import type { CapacitorConfig } from '@capacitor/cli';

const config: CapacitorConfig = {
  appId: 'com.apartsin.visionbook',
  appName: 'VisionBook',
  webDir: 'mobile/www',
  bundledWebRuntime: false,
  server: {
    androidScheme: 'https'
  }
};

export default config;
