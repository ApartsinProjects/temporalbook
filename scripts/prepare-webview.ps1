$ErrorActionPreference = 'Stop'

$root = Resolve-Path (Join-Path $PSScriptRoot '..')
$out = Join-Path $root 'mobile/www'

if (Test-Path $out) {
  Remove-Item -LiteralPath $out -Recurse -Force
}

New-Item -ItemType Directory -Force -Path $out | Out-Null

$dirs = @(
  'appendices',
  'capstone',
  'front-matter',
  'images',
  'part-1-foundations',
  'part-2-classical-forecasting',
  'part-3-temporal-deep-learning',
  'part-4-temporal-representation-learning',
  'part-5-uncertainty-online-adaptive',
  'part-6-sequential-decision-making',
  'part-7-building-intelligent-systems',
  'part-8-trustworthy-deployed',
  'part-9-applications-future',
  'scripts',
  'styles',
  'vendor'
)

foreach ($dir in $dirs) {
  $src = Join-Path $root $dir
  if (Test-Path $src) {
    Copy-Item -LiteralPath $src -Destination (Join-Path $out $dir) -Recurse -Force
  }
}

$files = @(
  '.nojekyll',
  'CNAME',
  'index.html',
  'robots.txt',
  'toc.html'
)

foreach ($file in $files) {
  $src = Join-Path $root $file
  if (Test-Path $src) {
    Copy-Item -LiteralPath $src -Destination (Join-Path $out $file) -Force
  }
}

Write-Host "Prepared bundled WebView assets at $out"
