export const meta = {
  name: 'taibook-full-sweep',
  description: 'Full 42-agent review/improve/validate sweep over one part of the book, per chapter',
  phases: [
    { title: 'Review', detail: '5 reviewer roles per chapter (cover all 42 agent checklists)' },
    { title: 'Integrate', detail: 'Chapter Lead applies fixes per section (surgical edits)' },
    { title: 'Validate', detail: 'Controller + Publication-QA structural validation per chapter' },
  ],
}

const ROOT = 'E:/Projects/taibook'
const SK = 'E:/Projects/claude-skills/book-skills/agents'
const CFG = `Read ${ROOT}/BOOK_CONFIG.md and ${ROOT}/CONFORMANCE_CHECKLIST.md once for house style (22-callout system, no-dash rule, tri-audience voice, from-scratch+library-shortcut code pairs).`

const GUARDRAILS = `HARD EDITING GUARDRAILS (a violation is worse than a missed improvement):
- Apply ONLY the concrete fixes listed for THIS section. Surgical edits, never a rewrite. Keep the author voice.
- NEVER alter, reorder, or delete existing: <a href> links, <img>/<figure> blocks and their numbering, KaTeX math ($...$, $$...$$), <pre><code> code blocks, callout <div class="callout ..."> structures, heading id= attributes.
- NO em-dash, en-dash, or double-hyphen anywhere. ASCII only. NO named HTML entities except &amp; &lt; &gt; &quot; &apos; (never &mdash; &hellip; &rsaquo; &middot; etc.).
- XHTML strict: SVG uses camelCase viewBox; alt= is plain text only (no tags/entities); every tag closed; no self-closing non-void tags like <div/>; <pre> must wrap <code>; code captions go BELOW the code as <div class="code-caption">.
- Do NOT add new math unless the section <head> already includes katex.min.css (it does). Do NOT insert new figures/images or renumber anything.
- Idempotent: if a fix says add an epigraph/bibliography/callout that already exists, skip it (do not duplicate).
- Do NOT touch the footer/boilerplate: the edition-line, the copyright line (&copy; ... &middot; ... Contents), chapter-nav, or header. Leave &copy; and &middot; exactly as they are (book-wide convention, normalized later at build time).
- Re-read the file immediately before each edit. Prioritize high and medium severity findings. Make every edit count.`

const REVIEW_SCHEMA = {
  type: 'object', additionalProperties: false,
  properties: {
    findings: {
      type: 'array',
      items: {
        type: 'object', additionalProperties: false,
        properties: {
          section: { type: 'string', description: 'exact section file name, e.g. section-1.2.html' },
          severity: { type: 'string', enum: ['high', 'med', 'low'] },
          category: { type: 'string' },
          issue: { type: 'string' },
          fix: { type: 'string', description: 'concrete, surgical fix the editor can apply' },
        },
        required: ['section', 'severity', 'category', 'issue', 'fix'],
      },
    },
  },
  required: ['findings'],
}

const EDIT_SCHEMA = {
  type: 'object', additionalProperties: false,
  properties: {
    section: { type: 'string' },
    applied: { type: 'number' },
    skipped: { type: 'number' },
    summary: { type: 'string' },
  },
  required: ['section', 'applied', 'skipped', 'summary'],
}

const VALIDATE_SCHEMA = {
  type: 'object', additionalProperties: false,
  properties: {
    chapter: { type: 'string' },
    pass: { type: 'boolean' },
    fixed: { type: 'array', items: { type: 'string' } },
    issues: { type: 'array', items: { type: 'string' } },
  },
  required: ['chapter', 'pass', 'fixed', 'issues'],
}

const ROLES = [
  {
    key: 'pedagogy',
    desc: `You embody book-skills reviewer agents 01,02,03,04,05,06,10,24,27 (curriculum, deep-explanation, teaching-flow, student-advocate, cognitive-load, example-analogy, misconception-analyst, aha-moment, memorability). For EACH section, flag where: a major concept lacks what/why/how/when depth; transitions or pacing around code/tables are abrupt; jargon is undefined or assumed knowledge is unflagged for the three audiences (practitioner, student, researcher); concept velocity is too high or there is a wall of text with no rest stop; an abstract concept has no concrete example or analogy; a common misconception or pitfall is missing; the section lacks a memorable hook or aha moment. Also note if stated learning objectives are not actually covered.`,
  },
  {
    key: 'technical',
    desc: `You embody book-skills reviewer agents 08,11,18,20,39,40 (code-pedagogy, fact-integrity, research-scientist, content-update-scout, figure-fact-checker, code-caption). For EACH section, flag where: code is not runnable/idiomatic or lacks pedagogical context or the from-scratch+library-shortcut pairing; a formula, claim, or definition is factually or mathematically wrong; a research-frontier callout or current method/library reference is missing or outdated as of 2026; a claim is stale or an API is deprecated; a figure/SVG contradicts or mismatches the prose; a code block lacks a caption below it. Be precise about the exact wrong value/claim and the correct one.`,
  },
  {
    key: 'prose',
    desc: `You embody book-skills reviewer agents 15,16,29,30,34 (style-voice, engagement, prose-clarity, readability-pacing, fun-injector). For EACH section, flag where: tone drifts from the house voice; the section is monotonous and could use a callout or rhythm change; a sentence is wordy/confusing and can be tightened (quote the sentence and give the tighter version); paragraph length or sentence variety hurts readability; a single apt, content-tied fun-note would help at a natural break (propose it, do not force humor).`,
  },
  {
    key: 'structure',
    desc: `You embody book-skills reviewer agents 12,13,14,19,21,37 (terminology, cross-reference AUDIT-ONLY, narrative-continuity, structural-architect, self-containment, controller). For the chapter, flag where: terminology or notation is inconsistent or drifts; a helpful cross-reference is missing OR an existing internal link is broken (report path; do NOT have the editor invent links); narrative/thread continuity breaks across sections; content is duplicated or out of dependency order; a prerequisite is used before being introduced or pointed to; structural conformance issues exist (heading hierarchy, callout classes, inline-style abuse, any em-dash/en-dash/double-hyphen). Tag each finding with the section it lives in.`,
  },
  {
    key: 'holistic',
    desc: `You embody book-skills reviewer agents 00,07,17,22,23,26,28,32,35 (chapter-lead, exercise-designer, senior-editor, opening-hook, project-catalyst, demo-simulation, skeptical-reader, epigraph-writer, bibliography). Reviewing the WHOLE chapter, flag where: the chapter opener/first section hook is weak; the hands-on lab or exercises are missing or poorly scoped; there is box/callout overload or visual imbalance (senior editor); a strong project or demo/simulation opportunity is unused; a skeptical reader would find the chapter indistinct or a claim undefended; the chapter epigraph is missing or not apt; the bibliography is missing or lacks real references. Tag each finding with the most relevant section file (use the chapter index or first section if chapter-wide).`,
  },
]

async function reviewChapter(ch) {
  const secList = ch.sections.join(', ')
  const reviews = await parallel(ROLES.map((r) => () =>
    agent(
      `You are a meticulous technical-book reviewer for "Building Temporal AI" at ${ROOT}.
${CFG}
${r.desc}

Chapter dir: ${ROOT}/${ch.dir}
Section files to review: ${secList}
Read the relevant section files (and the chapter index.html for chapter-wide context). Return ONLY high-value, concrete, actionable findings (skip nitpicks and anything already good). For each finding give the exact section file, a severity, a short category, the issue, and a concrete surgical fix an editor can apply WITHOUT rewriting the section. If the section is already strong, return few or no findings. Be efficient: read what you need, return findings. Under 14 tool calls.`,
      { label: `review:${r.key}:${ch.dir.split('/').pop()}`, phase: 'Review', schema: REVIEW_SCHEMA, agentType: 'general-purpose' }
    ).then((res) => (res && res.findings ? res.findings : []))
  ))
  const all = reviews.filter(Boolean).flat()
  return { ch, findings: all }
}

async function integrateChapter(prev) {
  const { ch, findings } = prev
  const bySection = {}
  for (const s of ch.sections) bySection[s] = []
  for (const f of findings) {
    if (bySection[f.section]) bySection[f.section].push(f)
    else (bySection[ch.sections[0]] = bySection[ch.sections[0]] || []).push(f)
  }
  const results = await parallel(ch.sections.map((sec) => () => {
    const fs = bySection[sec] || []
    if (!fs.length) return Promise.resolve({ section: sec, applied: 0, skipped: 0, summary: 'no findings' })
    const list = fs
      .sort((a, b) => ({ high: 0, med: 1, low: 2 }[a.severity] - { high: 0, med: 1, low: 2 }[b.severity]))
      .map((f, i) => `${i + 1}. [${f.severity}/${f.category}] ${f.issue}\n   FIX: ${f.fix}`)
      .join('\n')
    return agent(
      `You are the Chapter Lead (book-skills agent 00) in Implement mode for "Building Temporal AI" at ${ROOT}.
${CFG}
${GUARDRAILS}

File to edit: ${ROOT}/${ch.dir}/${sec}

Apply these reviewer findings to that ONE file, surgically:
${list}

Resolve conflicts sensibly, drop any fix that would violate the guardrails or duplicate existing content, and keep edits minimal and high-value. Re-read the file before editing. Under 16 tool calls. Report how many fixes you applied vs skipped and a one-line summary.`,
      { label: `integrate:${sec}`, phase: 'Integrate', schema: EDIT_SCHEMA, agentType: 'general-purpose' }
    )
  }))
  return { ch, edits: results.filter(Boolean) }
}

async function validateChapter(prev, ch) {
  const secList = ch.sections.join(', ')
  const v = await agent(
    `You are the Controller (book-skills agent 37) plus Publication-QA (agent 38) validating one chapter of "Building Temporal AI" at ${ROOT} after an editing pass.
Chapter dir: ${ROOT}/${ch.dir}
Section files: ${secList}

For each section file check and, where trivial and safe, FIX in place:
- em-dash / en-dash / double-hyphen anywhere (replace with comma/colon/parentheses/separate sentences) [FIX].
- illegal named HTML entities (&mdash; &hellip; &rsaquo; etc.) -> replace with plain ASCII [FIX]. DO NOT change &copy; or &middot; (book-wide footer convention, leave them).
- lowercase viewbox= on <svg> -> viewBox= [FIX].
- alt= containing tags or entities -> plain text [FIX].
- <pre> not wrapping <code>; code caption above instead of below.
- broken internal <a href> to a local file that does not exist; broken <img src> to a missing file.
- obvious unclosed-tag / malformed-HTML well-formedness problems introduced by editing.
Report issues you could NOT safely auto-fix as strings. Set pass=true only if zero unresolved issues remain. List what you fixed. Be efficient, under 16 tool calls.`,
    { label: `validate:${ch.dir.split('/').pop()}`, phase: 'Validate', schema: VALIDATE_SCHEMA, agentType: 'general-purpose' }
  )
  return { ch: ch.dir, findings: prev.findings ? prev.findings.length : undefined, edits: prev.edits, validation: v }
}

// INVENTORY: edit this block per part, then re-invoke the workflow.
const INV = {
  partName: 'part-9-applications-future',
  chapters: [
    { dir: 'part-9-applications-future/module-35-industrial-applications', sections: ['section-35.1.html', 'section-35.2.html', 'section-35.3.html', 'section-35.4.html', 'section-35.5.html', 'section-35.6.html'] },
    { dir: 'part-9-applications-future/module-36-general-temporal-intelligence', sections: ['section-36.1.html', 'section-36.2.html', 'section-36.3.html', 'section-36.4.html', 'section-36.5.html'] },
  ],
}

const chapters = INV.chapters
log(`Sweeping ${INV.partName}: ${chapters.length} chapters, ${chapters.reduce((a, c) => a + c.sections.length, 0)} sections`)

const out = await pipeline(chapters, reviewChapter, integrateChapter, validateChapter)

const summary = out.filter(Boolean).map((r) => ({
  chapter: r.ch,
  findings: r.findings,
  edits_applied: (r.edits || []).reduce((a, e) => a + (e.applied || 0), 0),
  validation_pass: r.validation ? r.validation.pass : null,
  unresolved: r.validation ? r.validation.issues : [],
}))
return summary
