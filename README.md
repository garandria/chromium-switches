| switch | description | variable | cpp condition | location |
| ------ | ----------- | -------- | ------------- | -------- |
| --webview-log-js-console-messages |  | kWebViewLogJsConsoleMessages |  | ../chromium/src/android_webview/common/aw_switches.cc |
| --webview-sandboxed-renderer |  | kWebViewSandboxedRenderer |  | ../chromium/src/android_webview/common/aw_switches.cc |
| --webview-disable-safebrowsing-support |  used to disable safebrowsing functionality in webview | kWebViewDisableSafebrowsingSupport |  | ../chromium/src/android_webview/common/aw_switches.cc |
| --webview-safebrowsing-block-all-resources |  Enables SafeBrowsing and causes WebView to treat all resources as malicious.  Use care: this will block all resources from loading. | kWebViewSafebrowsingBlockAllResources |  | ../chromium/src/android_webview/common/aw_switches.cc |
| --highlight-all-webviews |  Highlight the contents (including web contents) of all WebViews with a yellow  tint. This is useful for identifying WebViews in an Android application. | kHighlightAllWebViews |  | ../chromium/src/android_webview/common/aw_switches.cc |
| --net-log |  Enable net logging from WebView. This captures network activity for debugging  purposes, and stores the files in DevUi. | kNetLog |  | ../chromium/src/android_webview/common/aw_switches.cc |
| --webview-verbose-logging |  WebView will log additional debugging information to logcat, such as  variations and commandline state. | kWebViewVerboseLogging |  | ../chromium/src/android_webview/common/aw_switches.cc |
| --finch-seed-expiration-age |  The length of time in seconds that an app's copy of the variations seed  should be considered fresh. If an app's seed is older than this, a new seed  will be requested from WebView's IVariationsSeedServer. | kFinchSeedExpirationAge |  | ../chromium/src/android_webview/common/aw_switches.cc |
| --finch-seed-ignore-pending-download |  Forces WebView's service to always schedule a new variations seed download  job, even if one is already pending. | kFinchSeedIgnorePendingDownload |  | ../chromium/src/android_webview/common/aw_switches.cc |
| --finch-seed-no-charging-requirement |  Forces WebView's service to always schedule a new variations seed download  job, even if the device is not charging. Note this switch may be necessary  for testing on Android emulators as these are not always considered to be  charging. | kFinchSeedNoChargingRequirement |  | ../chromium/src/android_webview/common/aw_switches.cc |
| --finch-seed-min-download-period |  The minimum amount of time in seconds that WebView's service will wait  between two variations seed downloads from the variations server. | kFinchSeedMinDownloadPeriod |  | ../chromium/src/android_webview/common/aw_switches.cc |
| --finch-seed-min-update-period |  The minimum amount of time in seconds that the embedded WebView  implementation will wait between two requests to WebView's service for a new  variations seed. | kFinchSeedMinUpdatePeriod |  | ../chromium/src/android_webview/common/aw_switches.cc |
| --webview-enable-modern-cookie-same-site |  Enables modern SameSite cookie behavior (as opposed to legacy behavior). This  is used for WebView versions prior to when the modern behavior will be  enabled by default. This enables the same-site-by-default-cookies,  cookies-without-SameSite-must-be-secure, and schemeful-same-site features. | kWebViewEnableModernCookieSameSite |  | ../chromium/src/android_webview/common/aw_switches.cc |
| --webview-selective-image-inversion-darkening |  Enables use selective image inversion to automatically darken page, it will  be used when WebView is in dark mode, but website doesn't provide dark style. | kWebViewSelectiveImageInversionDarkening |  | ../chromium/src/android_webview/common/aw_switches.cc |
| --webview-fenced-frames |  Enables FencedFrames. This also enables PrivacySandboxAdsAPIsOverride. | kWebViewFencedFrames |  | ../chromium/src/android_webview/common/aw_switches.cc |
| --webview-enable-trust-tokens-component |  Enables downloading TrustTokenKeyCommitmentsComponent by the component  updater downloading service in nonembedded WebView. See  https:crbug.com/1170468. | kWebViewEnableTrustTokensComponent |  | ../chromium/src/android_webview/common/aw_switches.cc |
| --webview-tpcd-metadata-component |  Enables downloading TpcdMetadataComponentInstallerPolicy by the component  updater downloading service in nonembedded WebView. | kWebViewTpcdMetadaComponent |  | ../chromium/src/android_webview/common/aw_switches.cc |
| --webview-fps-component |  Enables downloading FirstPartySetsComponentInstallerPolicy by the component  updater downloading service in nonembedded WebView. | kWebViewFpsComponent |  | ../chromium/src/android_webview/common/aw_switches.cc |
| --webview-force-disable-3pcs |  Force disables 3rd party cookie for all apps. | kWebViewForceDisable3pcs |  | ../chromium/src/android_webview/common/aw_switches.cc |
| --webview-force-crash-java |  Enables crashes during WebView startup in the Java layer | kWebViewForceCrashJava |  | ../chromium/src/android_webview/common/aw_switches.cc |
| --webview-force-crash-native |  Enables crashes during WebView startup in the Native layer | kWebViewForceCrashNative |  | ../chromium/src/android_webview/common/aw_switches.cc |
| --webview-use-separate-resource-context |  Use WebView's context for resource lookups instead of the embedding app's. | kWebViewUseSeparateResourceContext |  | ../chromium/src/android_webview/common/aw_switches.cc |
| --debug-bsa |  Override and enable features useful for BSA library testing/debugging. | kDebugBsa |  | ../chromium/src/android_webview/common/aw_switches.cc |
| --webview-intercepted-cookie-header |  When enabled, the cookie header will be included in the request headers  for shouldInterceptRequest. | kWebViewInterceptedCookieHeader |  | ../chromium/src/android_webview/common/aw_switches.cc |
| switch | description | variable | cpp condition | location |
| ------ | ----------- | -------- | ------------- | -------- |
| switch | description | variable | cpp condition | location |
| ------ | ----------- | -------- | ------------- | -------- |
| switch | description | variable | cpp condition | location |
| ------ | ----------- | -------- | ------------- | -------- |
| --aggressive-cache-discard |  Please keep the order of these switches synchronized with the header file  (i.e. in alphabetical order). | kAggressiveCacheDiscardThreshold |  | ../chromium/src/ash/constants/ash_switches.cc |
| --allow-failed-policy-fetch-for-test |  If this flag is passed, failed policy fetches will not cause profile  initialization to fail. This is useful for tests because it means that  tests don't have to mock out the policy infrastructure. | kAllowFailedPolicyFetchForTest |  | ../chromium/src/ash/constants/ash_switches.cc |
| --allow-os-install |  When this flag is set, the OS installation UI can be accessed. This  allows the user to install from USB to disk. | kAllowOsInstall |  | ../chromium/src/ash/constants/ash_switches.cc |
| --almanac-api-url |  Override for the URL used for the ChromeOS Almanac API. Used for local  testing with a non-production server (e.g.  "--almanac-api-url=http:localhost:8000"). | kAlmanacApiUrl |  | ../chromium/src/ash/constants/ash_switches.cc |
| --always-enable-hdcp |  Causes HDCP of the specified type to always be enabled when an external  display is connected. Used for HDCP compliance testing on ChromeOS. | kAlwaysEnableHdcp |  | ../chromium/src/ash/constants/ash_switches.cc |
| --app-auto-launched |  Specifies whether an app launched in kiosk mode was auto launched with zero  delay. Used in order to properly restore auto-launched state during session  restore flow. | kAppAutoLaunched |  | ../chromium/src/ash/constants/ash_switches.cc |
| --app-mode-oem-manifest |  Path for app's OEM manifest file. | kAppOemManifestFile |  | ../chromium/src/ash/constants/ash_switches.cc |
| --arc-availability |  Signals ARC support status on this device. This can take one of the  following three values.  - none: ARC is not installed on this device. (default)  - installed: ARC is installed on this device, but not officially supported.    Users can enable ARC only when Finch experiment is turned on.  - officially-supported: ARC is installed and supported on this device. So    users can enable ARC via settings etc. | kArcAvailability |  | ../chromium/src/ash/constants/ash_switches.cc |
| --arc-available |  DEPRECATED: Please use --arc-availability=installed.  Signals the availability of the ARC instance on this device. | kArcAvailable |  | ../chromium/src/ash/constants/ash_switches.cc |
| --arc-block-keymint |  Switch that blocks KeyMint. When KeyMint is blocked, Keymaster is enabled. | kArcBlockKeyMint |  | ../chromium/src/ash/constants/ash_switches.cc |
| --arc-data-cleanup-on-start |  Flag that forces ARC data be cleaned on each start. | kArcDataCleanupOnStart |  | ../chromium/src/ash/constants/ash_switches.cc |
| --arc-disable-app-sync |  Flag that disables ARC app sync flow that installs some apps silently. Used  in autotests to resolve racy conditions. | kArcDisableAppSync |  | ../chromium/src/ash/constants/ash_switches.cc |
| --arc-disable-dexopt-cache |  Used in tests to disable DexOpt cache which is on by default. | kArcDisableDexOptCache |  | ../chromium/src/ash/constants/ash_switches.cc |
| --arc-disable-download-provider |  Flag that disables ARC download provider that prevents extra content to be  downloaded and installed in context of Play Store and GMS Core. | kArcDisableDownloadProvider |  | ../chromium/src/ash/constants/ash_switches.cc |
| --arc-disable-gms-core-cache |  Used in autotest to disable GMS-core caches which is on by default. | kArcDisableGmsCoreCache |  | ../chromium/src/ash/constants/ash_switches.cc |
| --arc-disable-locale-sync |  Flag that disables ARC locale sync with Android Container. Used in autotest  to prevent conditions when certain apps, including Play Store may get  restarted. Restarting Play Store may cause random test failures. Enabling  this flag would also forces ARC Container to use 'en-US' as a locale and  'en-US,en' as preferred languages. | kArcDisableLocaleSync |  | ../chromium/src/ash/constants/ash_switches.cc |
| --arc-disable-media-store-maintenance |  Used to disable GMS scheduling of media store periodic indexing and corpora  maintenance tasks. Used in performance tests to prevent running during  testing which can cause unstable results or CPU not idle pre-test failures. | kArcDisableMediaStoreMaintenance |  | ../chromium/src/ash/constants/ash_switches.cc |
| --arc-disable-play-auto-install |  Flag that disables ARC Play Auto Install flow that installs set of predefined  apps silently. Used in autotests to resolve racy conditions. | kArcDisablePlayAutoInstall |  | ../chromium/src/ash/constants/ash_switches.cc |
| --arc-disable-tts-cache |  Used in autotest to disable TTS cache which is on by default. | kArcDisableTtsCache |  | ../chromium/src/ash/constants/ash_switches.cc |
| --arc-use-dev-caches |  Flag that indicates ARC is using dev caches generated by data collector in  Uprev rather than caches from CrOS build stage for arccachesetup service. | kArcUseDevCaches |  | ../chromium/src/ash/constants/ash_switches.cc |
| --arc-erofs |  Flag that indicates ARC images are formatted with EROFS (go/arcvm-erofs). | kArcErofs |  | ../chromium/src/ash/constants/ash_switches.cc |
| --arc-force-mount-android-volumes-in-files |  Flag that forces Android volumes (DocumentsProviders and Play files) to be  mounted in the Files app. Used for testing. | kArcForceMountAndroidVolumesInFiles |  | ../chromium/src/ash/constants/ash_switches.cc |
| --arc-force-show-optin-ui |  Flag that forces the OptIn ui to be shown. Used in tests. | kArcForceShowOptInUi |  | ../chromium/src/ash/constants/ash_switches.cc |
| --arc-generate-play-auto-install |  Flag that enables developer options needed to generate an ARC Play Auto  Install roster. Used manually by developers. | kArcGeneratePlayAutoInstall |  | ../chromium/src/ash/constants/ash_switches.cc |
| --arc-host-ureadahead-mode |  Sets the mode of operation for ureadahead during ARC Container boot.  readahead (default) - used during production and is equivalent to no switch                        being set.  generate - used during Android Uprev data collector to pre-generate pack file             and upload to Google Cloud as build artifact for CrOS build image.  disabled - used for test purpose to disable ureadahead during ARC Container  boot. | kArcHostUreadaheadMode |  | ../chromium/src/ash/constants/ash_switches.cc |
| --arc-install-event-chrome-log-for-tests |  Write ARC++ install events to chrome log for integration test. | kArcInstallEventChromeLogForTests |  | ../chromium/src/ash/constants/ash_switches.cc |
| --arc-packages-cache-mode |  Used in autotest to specifies how to handle packages cache. Can be  copy - copy resulting packages.xml to the temporary directory.  skip-copy - skip initial packages cache setup and copy resulting packages.xml              to the temporary directory. | kArcPackagesCacheMode |  | ../chromium/src/ash/constants/ash_switches.cc |
| --arc-play-store-auto-update |  Used in autotest to forces Play Store auto-update state. Can be  on - auto-update is forced on.  off - auto-update is forced off. | kArcPlayStoreAutoUpdate |  | ../chromium/src/ash/constants/ash_switches.cc |
| --arc-scale |  Set the scale for ARC apps. This is in DPI. e.g. 280 DPI is ~ 1.75 device  scale factor.  See  https:source.android.com/compatibility/android-cdd#3_7_runtime_compatibility  for list of supported DPI values. | kArcScale |  | ../chromium/src/ash/constants/ash_switches.cc |
| --arc-start-mode |  Defines how to start ARC. This can take one of the following values:  - always-start automatically start with Play Store UI support.  - always-start-with-no-play-store automatically start without Play Store UI.  If it is not set, then ARC is started in default mode. | kArcStartMode |  | ../chromium/src/ash/constants/ash_switches.cc |
| --arc-tos-host-for-tests |  Sets ARC Terms Of Service hostname url for testing. | kArcTosHostForTests |  | ../chromium/src/ash/constants/ash_switches.cc |
| --arcvm-ureadahead-mode |  Sets the mode of operation for ureadahead during ARCVM boot. If this switch  is not set, ARCVM ureadahead will check for the presence and age of pack  file and reads ahead files to page cache for improved boot performance.  readahead (default) - used during production and is equivalent to no switch                        being set. This is used in tast test to explicitly turn                        on guest ureadahead (see |kArcDisableUreadahead|).  generate - used during Android Uprev data collector to pre-generate pack file             and upload to Google Cloud as build artifact for CrOS build image.  disabled - used for test purpose to disable ureadahead during ARCVM boot.             note, |kArcDisableUreadahead| also disables both, guest and host             parts of ureadahead. | kArcVmUreadaheadMode |  | ../chromium/src/ash/constants/ash_switches.cc |
| --arcvm-use-hugepages |  Madvises the kernel to use Huge Pages for guest memory. | kArcVmUseHugePages |  | ../chromium/src/ash/constants/ash_switches.cc |
| --ash-clear-fast-ink-buffer |  Clear the fast ink buffer upon creation. This is needed on some devices that  do not zero out new buffers. | kAshClearFastInkBuffer |  | ../chromium/src/ash/constants/ash_switches.cc |
| --ash-constrain-pointer-to-root |  Force the pointer (cursor) position to be kept inside root windows. | kAshConstrainPointerToRoot |  | ../chromium/src/ash/constants/ash_switches.cc |
| --ash-contextual-nudges-interval |  Overrides the minimum time that must pass between showing user contextual  nudges. Unit of time is in seconds. | kAshContextualNudgesInterval |  | ../chromium/src/ash/constants/ash_switches.cc |
| --ash-contextual-nudges-reset-shown-count |  Reset contextual nudge shown count on login. | kAshContextualNudgesResetShownCount |  | ../chromium/src/ash/constants/ash_switches.cc |
| --ash-debug-shortcuts |  Enable keyboard shortcuts useful for debugging. | kAshDebugShortcuts |  | ../chromium/src/ash/constants/ash_switches.cc |
| --ash-dev-shortcuts |  Enable keyboard shortcuts used by developers only. | kAshDeveloperShortcuts |  | ../chromium/src/ash/constants/ash_switches.cc |
| --ash-disable-touch-exploration-mode |  Disable the Touch Exploration Mode. Touch Exploration Mode will no longer be  turned on automatically when spoken feedback is enabled when this flag is  set. | kAshDisableTouchExplorationMode |  | ../chromium/src/ash/constants/ash_switches.cc |
| --ash-enable-magnifier-key-scroller |  Enables key bindings to scroll magnified screen. | kAshEnableMagnifierKeyScroller |  | ../chromium/src/ash/constants/ash_switches.cc |
| --ash-enable-palette-on-all-displays |  Enables the palette on every display, instead of only the internal one. | kAshEnablePaletteOnAllDisplays |  | ../chromium/src/ash/constants/ash_switches.cc |
| --enable-touchview |  If the flag is present, it indicates 1) the device has accelerometer and 2)  the device is a convertible device or a tablet device (thus is capable of  entering tablet mode). If this flag is not set, then the device is not  capable of entering tablet mode. For example, Samus has accelerometer, but  is not a covertible or tablet, thus doesn't have this flag set, thus can't  enter tablet mode. | kAshEnableTabletMode |  | ../chromium/src/ash/constants/ash_switches.cc |
| --enable-wayland-server |  Enable the wayland server. | kAshEnableWaylandServer |  | ../chromium/src/ash/constants/ash_switches.cc |
| --force-enable-stylus-tools |  Enables the stylus tools next to the status area. | kAshForceEnableStylusTools |  | ../chromium/src/ash/constants/ash_switches.cc |
| --force-status-area-collapsible |  Forces the status area to allow collapse/expand regardless of the current  state. | kAshForceStatusAreaCollapsible |  | ../chromium/src/ash/constants/ash_switches.cc |
| --ash-hide-notifications-for-factory |  Hides notifications that are irrelevant to Chrome OS device factory testing,  such as battery level updates. | kAshHideNotificationsForFactory |  | ../chromium/src/ash/constants/ash_switches.cc |
| --ash-no-nudges |  Hides educational nudges that can interfere with tast integration tests.  Somewhat similar to --no-first-run but affects system UI behavior, not  browser behavior. | kAshNoNudges |  | ../chromium/src/ash/constants/ash_switches.cc |
| --ash-power-button-position |  Power button position includes the power button's physical display side and  the percentage for power button center position to the display's  width/height in landscape_primary screen orientation. The value is a JSON  object containing a "position" property with the value "left", "right",  "top", or "bottom". For "left" and "right", a "y" property specifies the  button's center position as a fraction of the display's height (in [0.0,  1.0]) relative to the top of the display. For "top" and "bottom", an "x"  property gives the position as a fraction of the display's width relative to  the left side of the display. | kAshPowerButtonPosition |  | ../chromium/src/ash/constants/ash_switches.cc |
| --ash-side-volume-button-position |  The physical position info of the side volume button while in landscape  primary screen orientation. The value is a JSON object containing a "region"  property with the value "keyboard", "screen" and a "side" property with the  value "left", "right", "top", "bottom". | kAshSideVolumeButtonPosition |  | ../chromium/src/ash/constants/ash_switches.cc |
| --ash-touch-hud |  Enables the heads-up display for tracking touch points. | kAshTouchHud |  | ../chromium/src/ash/constants/ash_switches.cc |
| --force-tablet-mode |  Enables required things for the selected UI mode, regardless of whether the  Chromebook is currently in the selected UI mode. | kAshUiMode |  | ../chromium/src/ash/constants/ash_switches.cc |
| --clamshell |  Values for the kAshUiMode flag. | kAshUiModeClamshell |  | ../chromium/src/ash/constants/ash_switches.cc |
| --touch_view |  | kAshUiModeTablet |  | ../chromium/src/ash/constants/ash_switches.cc |
| --aura-legacy-power-button |  (Most) Chrome OS hardware reports ACPI power button releases correctly.  Standard hardware reports releases immediately after presses.  If set, we  lock the screen or shutdown the system immediately in response to a press  instead of displaying an interactive animation. | kAuraLegacyPowerButton |  | ../chromium/src/ash/constants/ash_switches.cc |
| --birch-is-evening |  Sets the birch ranker to assume it is evening for birch chip ranking  purposes. | kBirchIsEvening |  | ../chromium/src/ash/constants/ash_switches.cc |
| --birch-is-morning |  Sets the birch ranker to assume it is morning for birch chip ranking  purposes. | kBirchIsMorning |  | ../chromium/src/ash/constants/ash_switches.cc |
| --campbell-key |  Switch used to pass in a secret key for Campbell feature. Unless the correct  secret key is provided, Campbell feature will remain disabled, regardless of  the state of the associated feature flag. | kCampbellKey |  | ../chromium/src/ash/constants/ash_switches.cc |
| --cellular-first |  If this flag is set, it indicates that this device is a "Cellular First"  device. Cellular First devices use cellular telephone data networks as  their primary means of connecting to the internet.  Setting this flag has two consequences:  1. Cellular data roaming will be enabled by default.  2. UpdateEngine will be instructed to allow auto-updating over cellular     data connections. | kCellularFirst |  | ../chromium/src/ash/constants/ash_switches.cc |
| --child-wallpaper-large |  Default large wallpaper to use for kids accounts (as path to trusted,  non-user-writable JPEG file). | kChildWallpaperLarge |  | ../chromium/src/ash/constants/ash_switches.cc |
| --child-wallpaper-small |  Default small wallpaper to use for kids accounts (as path to trusted,  non-user-writable JPEG file). | kChildWallpaperSmall |  | ../chromium/src/ash/constants/ash_switches.cc |
| --conch-key |  Switch used to pass in a secret key for Conch. Unless the correct secret key  is provided, Conch feature will remain disabled, regardless of the state of  the associated feature flag. | kConchKey |  | ../chromium/src/ash/constants/ash_switches.cc |
| --cros-region |  Forces CrOS region value. | kCrosRegion |  | ../chromium/src/ash/constants/ash_switches.cc |
| --cryptohome-recovery-service-base-url |  Overrides the base url for the Cryptohome recovery service. | kCryptohomeRecoveryServiceBaseUrl |  | ../chromium/src/ash/constants/ash_switches.cc |
| --cryptohome-recovery-use-test-env |  Forces cryptohome recovery process to use test environment (test keys /  URLs). | kCryptohomeRecoveryUseTestEnvironment |  | ../chromium/src/ash/constants/ash_switches.cc |
| --cryptohome-use-authsession |  Controls if AuthSession API should be used when interacting with cryptohomed. | kCryptohomeUseAuthSession |  | ../chromium/src/ash/constants/ash_switches.cc |
| --cryptohome-use-old-encryption-for-testing |  Forces cryptohome to create new users using old (ecryptfs) encryption.  This switch can be used to set up configurations that can be used to  test encryption migration scenarios. | kCryptohomeUseOldEncryptionForTesting |  | ../chromium/src/ash/constants/ash_switches.cc |
| --cryptohome-ignore-cleanup-ownership-for-testing |  Normally the cryptohome without any any authentication factors  is considered corrupted. Special mechanism would detect such situation  during user creation and remove such users. If such user is an owner  the power wash should be triggered instead. However, if such event happens  in tests, all logs would be lost, and it would be difficult to investigate  exact reason behind the Owner user being misconfigured.  This flag prevents triggering powerwash in such cases, simple user removal  would be triggered instead. | kCryptohomeIgnoreCleanupOwnershipForTesting |  | ../chromium/src/ash/constants/ash_switches.cc |
| --default-wallpaper-is-oem |  Indicates that the wallpaper images specified by  kAshDefaultWallpaper{Large,Small} are OEM-specific (i.e. they are not  downloadable from Google). | kDefaultWallpaperIsOem |  | ../chromium/src/ash/constants/ash_switches.cc |
| --default-wallpaper-large |  Default large wallpaper to use (as path to trusted, non-user-writable JPEG  file). | kDefaultWallpaperLarge |  | ../chromium/src/ash/constants/ash_switches.cc |
| --default-wallpaper-small |  Default small wallpaper to use (as path to trusted, non-user-writable JPEG  file). | kDefaultWallpaperSmall |  | ../chromium/src/ash/constants/ash_switches.cc |
| --defer-external-display-timeout |  Interval in seconds to wait for a display to reconnect while unlocking or  logging in with a closed lid. | kDeferExternalDisplayTimeout |  | ../chromium/src/ash/constants/ash_switches.cc |
| --demo-mode-enrolling-username |  Test Organization Unit (OU) user to use for demo mode. Only pass the part  before "@cros-demo-mode.com". | kDemoModeEnrollingUsername |  | ../chromium/src/ash/constants/ash_switches.cc |
| --demo-mode-force-arc-offline-provision |  Force ARC provision to take code path for offline demo mode. | kDemoModeForceArcOfflineProvision |  | ../chromium/src/ash/constants/ash_switches.cc |
| --demo-mode-highlights-extension |  App ID to use for highlights app in demo mode. | kDemoModeHighlightsApp |  | ../chromium/src/ash/constants/ash_switches.cc |
| --demo-mode-screensaver-extension |  App ID to use for screensaver app in demo mode. | kDemoModeScreensaverApp |  | ../chromium/src/ash/constants/ash_switches.cc |
| --demo-mode-swa-content-directory |  Directory from which to fetch the demo mode SWA content (instead of  downloading from Omaha). | kDemoModeSwaContentDirectory |  | ../chromium/src/ash/constants/ash_switches.cc |
| --demo-mode-resource-directory |  Directory from which to fetch the demo mode resource content (instead of  downloading from Omaha). | kDemoModeResourceDirectory |  | ../chromium/src/ash/constants/ash_switches.cc |
| --derelict-detection-timeout |  Time in seconds before a machine at OOBE is considered derelict. | kDerelictDetectionTimeout |  | ../chromium/src/ash/constants/ash_switches.cc |
| --derelict-idle-timeout |  Time in seconds before a derelict machines starts demo mode. | kDerelictIdleTimeout |  | ../chromium/src/ash/constants/ash_switches.cc |
| --disable-arc-cpu-restriction |  Prevents any CPU restrictions being set on ARC[VM]. Only meant to be used by  tests as some tests may time out if the ARC container is throttled. | kDisableArcCpuRestriction |  | ../chromium/src/ash/constants/ash_switches.cc |
| --disable-arc-opt-in-verification |  Disables ARC Opt-in verification process and ARC is enabled by default. | kDisableArcOptInVerification |  | ../chromium/src/ash/constants/ash_switches.cc |
| --disable-birch-weather-api-for-testing |  Disables the Weather API from being called by Birch. Allows fake users in  tast tests to avoid making API calls using an invalid GAIA ID, which causes  errors on the weather server side. | kDisableBirchWeatherApiForTesting |  | ../chromium/src/ash/constants/ash_switches.cc |
| --disable-demo-mode |  Disables the Chrome OS demo. | kDisableDemoMode |  | ../chromium/src/ash/constants/ash_switches.cc |
| --disable-device-disabling |  If this switch is set, the device cannot be remotely disabled by its owner. | kDisableDeviceDisabling |  | ../chromium/src/ash/constants/ash_switches.cc |
| --disable-drive-fs-for-testing |  Disables DriveFS for testing purposes, used in tast testing and only on test  images. | kDisableDriveFsForTesting |  | ../chromium/src/ash/constants/ash_switches.cc |
| --disable-fine-grained-time-zone-detection |  Disables fine grained time zone detection. | kDisableFineGrainedTimeZoneDetection |  | ../chromium/src/ash/constants/ash_switches.cc |
| --disable-first-run-ui |  Disables first-run UI from being shown. | kDisableFirstRunUI |  | ../chromium/src/ash/constants/ash_switches.cc |
| --disable-gaia-services |  Disables GAIA services such as enrollment and OAuth session restore. Used by  'fake' telemetry login. | kDisableGaiaServices |  | ../chromium/src/ash/constants/ash_switches.cc |
| --disable-hid-detection-on-oobe |  Disables HID-detection OOBE screen. | kDisableHIDDetectionOnOOBEForTesting |  | ../chromium/src/ash/constants/ash_switches.cc |
| --disable-lacros-keep-alive |  Disables the Lacros keep alive for testing. | kDisableLacrosKeepAliveForTesting |  | ../chromium/src/ash/constants/ash_switches.cc |
| --disable-login-animations |  Avoid doing expensive animations upon login. | kDisableLoginAnimations |  | ../chromium/src/ash/constants/ash_switches.cc |
| --disable-login-lacros-opening |  If Lacros is set to the primary web browser, on session login, it is  automatically launched. This disables the feature, i.e., if this flag is  set, even if lacros is the primary web browser, it won't automatically  launch on session login. This is for testing purpose, specifically for Tast. | kDisableLoginLacrosOpening |  | ../chromium/src/ash/constants/ash_switches.cc |
| --disable-machine-cert-request |  Disables requests for an enterprise machine certificate during attestation. | kDisableMachineCertRequest |  | ../chromium/src/ash/constants/ash_switches.cc |
| --disable-oobe-chromevox-hint-timer-for-testing |  Disables the ChromeVox hint idle detection in OOBE, which can lead to  unexpected behavior during tests. | kDisableOOBEChromeVoxHintTimerForTesting |  | ../chromium/src/ash/constants/ash_switches.cc |
| --disable-oobe-network-screen-skipping-for-testing |  Disables network screen skip check which is based on ethernet connection. | kDisableOOBENetworkScreenSkippingForTesting |  | ../chromium/src/ash/constants/ash_switches.cc |
| --disable-per-user-timezone |  Disables per-user timezone. | kDisablePerUserTimezone |  | ../chromium/src/ash/constants/ash_switches.cc |
| --disable-rollback-option |  Disables rollback option on reset screen. | kDisableRollbackOption |  | ../chromium/src/ash/constants/ash_switches.cc |
| --disable-signin-frame-client-certs |  Disables client certificate authentication on the sign-in frame on the Chrome  OS sign-in profile.  TODO(crbug.com/41389560): Remove this flag when reaching endpoints that  request client certs does not hang anymore when there is no system token yet. | kDisableSigninFrameClientCerts |  | ../chromium/src/ash/constants/ash_switches.cc |
| --disable-volume-adjust-sound |  Disables volume adjust sound. | kDisableVolumeAdjustSound |  | ../chromium/src/ash/constants/ash_switches.cc |
| --enable-arc |  DEPRECATED. Please use --arc-availability=officially-supported.  Enables starting the ARC instance upon session start. | kEnableArc |  | ../chromium/src/ash/constants/ash_switches.cc |
| --enable-arcvm |  Enables ARCVM. | kEnableArcVm |  | ../chromium/src/ash/constants/ash_switches.cc |
| --enable-arcvm-dlc |  Enables ARCVM DLC. | kEnableArcVmDlc |  | ../chromium/src/ash/constants/ash_switches.cc |
| --enable-arcvm-rt-vcpu |  Enables ARCVM realtime VCPU feature. | kEnableArcVmRtVcpu |  | ../chromium/src/ash/constants/ash_switches.cc |
| --enable-ash-debug-browser |  Adds ash-browser back to launcher, even if in LacrosOnly mode. | kEnableAshDebugBrowser |  | ../chromium/src/ash/constants/ash_switches.cc |
| --enable-birch-weather-api-for-testing-override |  Used to override `kDisableBirchWeatherApiForTesting` for specific tast tests. | kEnableBirchWeatherApiForTestingOverride |  | ../chromium/src/ash/constants/ash_switches.cc |
| --enable-cast-receiver |  Enables the Cast Receiver. | kEnableCastReceiver |  | ../chromium/src/ash/constants/ash_switches.cc |
| --enable-dim-shelf |  Enables Shelf Dimming for ChromeOS. | kEnableDimShelf |  | ../chromium/src/ash/constants/ash_switches.cc |
| --enable-extension-assets-sharing |  Enables sharing assets for installed default apps. | kEnableExtensionAssetsSharing |  | ../chromium/src/ash/constants/ash_switches.cc |
| --enable-houdini |  Enables the use of 32-bit Houdini library for ARM binary translation. | kEnableHoudini |  | ../chromium/src/ash/constants/ash_switches.cc |
| --enable-houdini64 |  Enables the use of 64-bit Houdini library for ARM binary translation. | kEnableHoudini64 |  | ../chromium/src/ash/constants/ash_switches.cc |
| --enable-houdini-dlc |  Enables the use of Houdini DLC library for ARM binary translation. This is  independent of choosing between the 32-bit vs 64-bit Houdini library. Houdini  DLC library will be downloaded and installed at run-time instead of at build  time. | kEnableHoudiniDlc |  | ../chromium/src/ash/constants/ash_switches.cc |
| --enable-ndk-translation |  Enables the use of 32-bit NDK translation library for ARM binary translation. | kEnableNdkTranslation |  | ../chromium/src/ash/constants/ash_switches.cc |
| --enable-ndk-translation64 |  Enables the use of 64-bit NDK translation library for ARM binary translation. | kEnableNdkTranslation64 |  | ../chromium/src/ash/constants/ash_switches.cc |
| --enable-oobe-chromevox-hint-timer-for-dev-mode |  Enables the ChromeVox hint in OOBE for dev mode. This flag is used  to override the default dev mode behavior of disabling the feature.  If both kEnableOOBEChromeVoxHintForDevMode and  kDisableOOBEChromeVoxHintTimerForTesting are present, the ChromeVox hint  will be disabled, since the latter flag takes precedence over the former. | kEnableOOBEChromeVoxHintForDevMode |  | ../chromium/src/ash/constants/ash_switches.cc |
| --enable-oobe-test-api |  Enables OOBE testing API for tast tests. | kEnableOobeTestAPI |  | ../chromium/src/ash/constants/ash_switches.cc |
| --enable-requisition-edits |  Enables configuring the OEM Device Requisition in the OOBE. | kEnableRequisitionEdits |  | ../chromium/src/ash/constants/ash_switches.cc |
| --enable-tablet-form-factor |  Enables tablet form factor. | kEnableTabletFormFactor |  | ../chromium/src/ash/constants/ash_switches.cc |
| --enable-touch-calibration-setting |  Enables the touch calibration option in MD settings UI for valid touch  displays. | kEnableTouchCalibrationSetting |  | ../chromium/src/ash/constants/ash_switches.cc |
| --enable-touchpad-three-finger-click |  Enables touchpad three-finger-click as middle button. | kEnableTouchpadThreeFingerClick |  | ../chromium/src/ash/constants/ash_switches.cc |
| --enterprise-disable-arc |  Disables ARC for managed accounts. | kEnterpriseDisableArc |  | ../chromium/src/ash/constants/ash_switches.cc |
| --enterprise-force-manual-enrollment-in-test-builds |  Whether to force manual enrollment instead of trying cert based enrollment.  Only works on test builds. | kEnterpriseForceManualEnrollmentInTestBuilds |  | ../chromium/src/ash/constants/ash_switches.cc |
| --enterprise-enable-unified-state-determination |  Whether to enable unified state determination. | kEnterpriseEnableUnifiedStateDetermination |  | ../chromium/src/ash/constants/ash_switches.cc |
| --enterprise-enable-forced-re-enrollment |  Whether to enable forced enterprise re-enrollment. | kEnterpriseEnableForcedReEnrollment |  | ../chromium/src/ash/constants/ash_switches.cc |
| --enterprise-enable-forced-re-enrollment-on-flex |  Whether to enable forced enterprise re-enrollment on Flex. | kEnterpriseEnableForcedReEnrollmentOnFlex |  | ../chromium/src/ash/constants/ash_switches.cc |
| --enterprise-enable-initial-enrollment |  Whether to enable initial enterprise enrollment. | kEnterpriseEnableInitialEnrollment |  | ../chromium/src/ash/constants/ash_switches.cc |
| --enterprise-enrollment-initial-modulus |  Power of the power-of-2 initial modulus that will be used by the  auto-enrollment client. E.g. "4" means the modulus will be 2^4 = 16. | kEnterpriseEnrollmentInitialModulus |  | ../chromium/src/ash/constants/ash_switches.cc |
| --enterprise-enrollment-modulus-limit |  Power of the power-of-2 maximum modulus that will be used by the  auto-enrollment client. | kEnterpriseEnrollmentModulusLimit |  | ../chromium/src/ash/constants/ash_switches.cc |
| --disallow-policy-block-dev-mode |  Disallow blocking developer mode through enterprise device policy:  - Fail enterprise enrollment if enrolling would block dev mode.  - Don't apply new device policy if it would block dev mode.  This is only usable on test builds. | kDisallowPolicyBlockDevMode |  | ../chromium/src/ash/constants/ash_switches.cc |
| --eol-ignore-profile-creation-time |  Ignore the profile creation time when determining whether to show the end of  life notification incentive. This is meant to make manual testing easier. | kEolIgnoreProfileCreationTime |  | ../chromium/src/ash/constants/ash_switches.cc |
| --eol-reset-dismissed-prefs |  Reset the end of life notification prefs to their default value, at the  start of the user session. This is meant to make manual testing easier. | kEolResetDismissedPrefs |  | ../chromium/src/ash/constants/ash_switches.cc |
| --extension-install-event-chrome-log-for-tests |  Write extension install events to chrome log for integration test. | kExtensionInstallEventChromeLogForTests |  | ../chromium/src/ash/constants/ash_switches.cc |
| --external-metrics-collection-interval |  Interval in seconds between Chrome reading external metrics from  /var/lib/metrics/uma-events. | kExternalMetricsCollectionInterval |  | ../chromium/src/ash/constants/ash_switches.cc |
| --extra-web-apps-dir |  Name of a subdirectory of the main external web apps directory which  additional web apps configs should be loaded from. Used to load  device-specific web apps. | kExtraWebAppsDir |  | ../chromium/src/ash/constants/ash_switches.cc |
| --fake-arc-recommended-apps-for-testing |  Specifies number of recommended (fake) ARC apps during user onboarding.  App descriptions are generated locally instead of being fetched from server.  Limited to ChromeOS-on-linux and test images only. | kFakeArcRecommendedAppsForTesting |  | ../chromium/src/ash/constants/ash_switches.cc |
| --fake-drivefs-launcher-chroot-path |  An absolute path to the chroot hosting the DriveFS to use. This is only used  when running on Linux, i.e. when IsRunningOnChromeOS() returns false. | kFakeDriveFsLauncherChrootPath |  | ../chromium/src/ash/constants/ash_switches.cc |
| --fake-drivefs-launcher-socket-path |  A relative path to socket to communicat with the fake DriveFS launcher within  the chroot specified by kFakeDriveFsLauncherChrootPath. This is only used  when running on Linux, i.e. when IsRunningOnChromeOS() returns false. | kFakeDriveFsLauncherSocketPath |  | ../chromium/src/ash/constants/ash_switches.cc |
| --fingerprint-sensor-location |  Fingerprint sensor location indicates the physical sensor's location. The  value is a string with possible values: "power-button-top-left",  "keyboard-bottom-left", keyboard-bottom-right", "keyboard-top-right". | kFingerprintSensorLocation |  | ../chromium/src/ash/constants/ash_switches.cc |
| --first-exec-after-boot |  Passed to Chrome the first time that it's run after the system boots.  Not passed on restart after sign out. | kFirstExecAfterBoot |  | ../chromium/src/ash/constants/ash_switches.cc |
| --force-birch-fake-coral |  Forces a chip with fake coral data to be shown. | kForceBirchFakeCoral |  | ../chromium/src/ash/constants/ash_switches.cc |
| --force-birch-fetch |  Forces a fetch of Birch data whenever an informed restore session starts. | kForceBirchFetch |  | ../chromium/src/ash/constants/ash_switches.cc |
| --force-birch-release-notes |  If set, skips the logic in birch release notes provider and always sets  release notes item. | kForceBirchReleaseNotes |  | ../chromium/src/ash/constants/ash_switches.cc |
| --force-cryptohome-recovery-for-testing |  Forces fetching tokens for Cryptohome Recovery. | kForceCryptohomeRecoveryForTesting |  | ../chromium/src/ash/constants/ash_switches.cc |
| --force-first-run-ui |  Forces first-run UI to be shown for every login. | kForceFirstRunUI |  | ../chromium/src/ash/constants/ash_switches.cc |
| --force-hwid-check-result-for-test |  Forces Hardware ID check (happens during OOBE) to fail or succeed. Possible  values: "failure" or "success". Should be used only for testing. | kForceHWIDCheckResultForTest |  | ../chromium/src/ash/constants/ash_switches.cc |
| --force-happiness-tracking-system |  Force enables the Happiness Tracking System for the device. This ignores  user profile check and time limits and shows the notification every time  for any type of user. Should be used only for testing. | kForceHappinessTrackingSystem |  | ../chromium/src/ash/constants/ash_switches.cc |
| --force-lacros-launch-at-login-screen-for-testing |  Forces prelaunching Lacros at login screen regardless  of whether there are or aren't users with Lacros enabled. | kForceLacrosLaunchAtLoginScreenForTesting |  | ../chromium/src/ash/constants/ash_switches.cc |
| --force-launch-browser |  Forces FullRestoreService to launch browser for telemetry tests. | kForceLaunchBrowser |  | ../chromium/src/ash/constants/ash_switches.cc |
| --force-login-manager-in-tests |  Usually in browser tests the usual login manager bringup is skipped so that  tests can change how it's brought up. This flag disables that. | kForceLoginManagerInTests |  | ../chromium/src/ash/constants/ash_switches.cc |
| --force-show-cursor |  Forces the cursor to be shown even if we are mimicking touch events. Note  that cursor changes are locked when using this switch. | kForceShowCursor |  | ../chromium/src/ash/constants/ash_switches.cc |
| --force-show-release-track |  Force the "release track" UI to show in the system tray. Simulates the system  being on a non-stable release channel with feedback enabled. | kForceShowReleaseTrack |  | ../chromium/src/ash/constants/ash_switches.cc |
| --force-tablet-power-button |  If set, tablet-like power button behavior (i.e. tapping the button turns the  screen off) is used even if the device is in laptop mode. | kForceTabletPowerButton |  | ../chromium/src/ash/constants/ash_switches.cc |
| --form-factor |  Specifies the device's form factor. If provided, this flag overrides the  value from the LSB release info. Possible values are: "CHROMEBASE",  "CHROMEBIT", "CHROMEBOOK", "REFERENCE", "CHROMEBOX" | kFormFactor |  | ../chromium/src/ash/constants/ash_switches.cc |
| --growth-campaigns |  Specifies campaigns to override for testing. | kGrowthCampaigns |  | ../chromium/src/ash/constants/ash_switches.cc |
| --growth-campaigns-clear-events-at-session-start |  Clear all growth framework Feature Engagement events at session start for  testing. | kGrowthCampaignsClearEventsAtSessionStart |  | ../chromium/src/ash/constants/ash_switches.cc |
| --growth-campaigns-path |  Path for which to load growth campaigns file for testing (instead of  downloading from Omaha). | kGrowthCampaignsPath |  | ../chromium/src/ash/constants/ash_switches.cc |
| --growth-campaigns-current-time |  Specifies the device current time in `SecondsSinceUnixEpoch` format for  testing. | kGrowthCampaignsCurrentTimeSecondsSinceUnixEpoch |  | ../chromium/src/ash/constants/ash_switches.cc |
| --growth-campaigns-registered-time |  Specifies the device registered time in `SecondsSinceUnixEpoch` format for  testing. | kGrowthCampaignsRegisteredTimeSecondsSinceUnixEpoch |  | ../chromium/src/ash/constants/ash_switches.cc |
| --growth-campaigns-delayed-trigger-time-in-secs |  Specifies the delay time to trigger campaigns for testing. | kGrowthCampaignsDelayedTriggerTimeInSecs |  | ../chromium/src/ash/constants/ash_switches.cc |
| --bwsi |  Indicates that the browser is in "browse without sign-in" (Guest session)  mode. Should completely disable extensions, sync and bookmarks. | kGuestSession |  | ../chromium/src/ash/constants/ash_switches.cc |
| --guest-wallpaper-large |  Large wallpaper to use in guest mode (as path to trusted, non-user-writable  JPEG file). | kGuestWallpaperLarge |  | ../chromium/src/ash/constants/ash_switches.cc |
| --guest-wallpaper-small |  Small wallpaper to use in guest mode (as path to trusted, non-user-writable  JPEG file). | kGuestWallpaperSmall |  | ../chromium/src/ash/constants/ash_switches.cc |
| --has-chromeos-keyboard |  If set, the system is a Chromebook with a "standard Chrome OS keyboard",  which generally means one with a Search key in the standard Caps Lock  location above the Left Shift key. It should be unset for Chromebooks with  both Search and Caps Lock keys (e.g. stout) and for devices like Chromeboxes  that only use external keyboards. | kHasChromeOSKeyboard |  | ../chromium/src/ash/constants/ash_switches.cc |
| --has-hps |  Whether this device that has hps. | kHasHps |  | ../chromium/src/ash/constants/ash_switches.cc |
| --has-internal-stylus |  Whether this device has an internal stylus. | kHasInternalStylus |  | ../chromium/src/ash/constants/ash_switches.cc |
| --has-number-pad |  If set, the system is a Chromebook with a number pad as part of its internal  keyboard. | kHasNumberPad |  | ../chromium/src/ash/constants/ash_switches.cc |
| --homedir |  Defines user homedir. This defaults to primary user homedir. | kHomedir |  | ../chromium/src/ash/constants/ash_switches.cc |
| --ignore-arcvm-dev-conf |  If set, the "ignore_dev_conf" field in StartArcVmRequest message will  consequently be set such that all development configuration directives in  /usr/local/vms/etc/arcvm_dev.conf will be ignored during ARCVM start. | kIgnoreArcVmDevConf |  | ../chromium/src/ash/constants/ash_switches.cc |
| --ignore-unknown-auth-factors |  If true, chrome would silently ignore unknown auth factor types  instead of crashing. | kIgnoreUnknownAuthFactors |  | ../chromium/src/ash/constants/ash_switches.cc |
| --ignore-user-profile-mapping-for-tests |  If true, profile selection in UserManager will always return active user's  profile.  TODO(nkostlyev): http:crbug.com/364604 - Get rid of this switch after we  turn on multi-profile feature on ChromeOS. | kIgnoreUserProfileMappingForTests |  | ../chromium/src/ash/constants/ash_switches.cc |
| --stabilize-time-dependent-view-for-tests |  If true, the time dependent views (such as the time view) show with the  predefined fixed time. | kStabilizeTimeDependentViewForTests |  | ../chromium/src/ash/constants/ash_switches.cc |
| --install-log-fast-upload-for-tests |  Decreases delay in uploading installation event logs for integration test. | kInstallLogFastUploadForTests |  | ../chromium/src/ash/constants/ash_switches.cc |
| --kiosk-splash-screen-min-time-seconds |  Minimum time the kiosk splash screen will be shown in seconds. | kKioskSplashScreenMinTimeSeconds |  | ../chromium/src/ash/constants/ash_switches.cc |
| --lacros-availability-ignore |  When this flag is set, the lacros-availability policy is ignored. | kLacrosAvailabilityIgnore |  | ../chromium/src/ash/constants/ash_switches.cc |
| --lacros-chrome-additional-args |  If this switch is set, then ash-chrome will pass additional arguments when  launching lacros-chrome. The string '####' is used as a delimiter. Example:  --lacros-chrome-additional-args="--foo=5####--bar=/tmp/dir name". Will  result in two arguments passed to lacros-chrome:    --foo=5    --bar=/tmp/dir name | kLacrosChromeAdditionalArgs |  | ../chromium/src/ash/constants/ash_switches.cc |
| --lacros-chrome-additional-args-file |  If this switch is set, then ash-chrome will read from the provided path  and pass additional arguments when launching lacros-chrome. Each non-empty  line in the file will be treated as an argument. Example file contents:    --foo=5    --bar=/tmp/dir name | kLacrosChromeAdditionalArgsFile |  | ../chromium/src/ash/constants/ash_switches.cc |
| --lacros-chrome-additional-env |  Additional environment variables set for lacros-chrome. The string '####' is  used as a delimiter. For example:  --lacros-chrome-additional-env=WAYLAND_DEBUG=client####FOO=bar  will enable Wayland protocol logging and set FOO=bar. | kLacrosChromeAdditionalEnv |  | ../chromium/src/ash/constants/ash_switches.cc |
| --lacros-chrome-path |  If this switch is set, then ash-chrome will exec the lacros-chrome binary  from the indicated path rather than from component updater. Note that the  path should be to a directory that contains a binary named 'chrome'. | kLacrosChromePath |  | ../chromium/src/ash/constants/ash_switches.cc |
| --lacros-mojo-socket-for-testing |  If set, ash-chrome will drop a Unix domain socket to wait for a process to  connect to it, and the connection will be used to request file descriptors  from ash-chrome, and when the process forks to start a lacros-chrome, the  obtained file descriptor will be used by lacros-chrome to set up the mojo  connection with ash-chrome. There are mainly two use cases:  1. Test launcher to run browser tests in testing environment.  2. A terminal to start lacros-chrome with a debugger. | kLacrosMojoSocketForTesting |  | ../chromium/src/ash/constants/ash_switches.cc |
| --lacros-selection-policy-ignore |  When this flag is set, the lacros-selection policy is ignored. | kLacrosSelectionPolicyIgnore |  | ../chromium/src/ash/constants/ash_switches.cc |
| --extensions-run-in-ash-and-lacros |  If set, it passes the ids of additional extensions allowed to run in  both ash and lacros when lacros is enabled. The ids are separated by ",".  This should only used for testing.  Note: The ids passed to this switch and the ids passed to  kExtensionsRunInAshOnly should be mutually exclusive, i.e., without overlaps.  If any extension passed to this switch are to be published to app service,  it must be listed in one of the app service block switches so that  it won't be published to app service in both ash and lacros. Currently,  we don't have any use case with an extension running in both ash and lacros  to be published to app service, therefore, we haven't defined the app service  block switch for extensions. | kExtensionsRunInBothAshAndLacros |  | ../chromium/src/ash/constants/ash_switches.cc |
| --extension-apps-run-in-ash-and-lacros |  If set, it passes the ids of additional extension apps allowed to run in  in both ash and lacros when lacros is enabled. The ids are separated by ",".  This should only used for testing.  Note: The ids passed to this switch and the ids passed to  kExtensionAppsRunInAshOnly should be mutually exclusive, i.e., without  overlaps. If any extension app passed to this switch are to be publisedh to  app service, it must be listed in one of the app service block switches so  that it won't be published to app service in both ash and lacros. Currently,  we only have the use case of an extension app running in both ash and lacros  to be published to app service in lacros only, therefore, we only add the  kExtensionAppsBlockForAppServiceInAsh switch. | kExtensionAppsRunInBothAshAndLacros |  | ../chromium/src/ash/constants/ash_switches.cc |
| --extensions-run-in-ash-only |  If set, it passes the ids of the additional extensions allowed to run in  ash only when lacros is enabled. The ids are separated by ",".  This should only used for testing. | kExtensionsRunInAshOnly |  | ../chromium/src/ash/constants/ash_switches.cc |
| --extension-apps-run-in-ash-only |  If set, it passes the ids of the additional extension apps allowed to run in  ash only when lacros is enabled. The ids are separated by ",".  This should only used for testing. | kExtensionAppsRunInAshOnly |  | ../chromium/src/ash/constants/ash_switches.cc |
| --extension-apps-block-for-app-service-in-ash |  If set, it passes the ids of the extension apps blocked for app service  in ash when lacros is enabled. The ids are separated by ",".  This should only used for testing. | kExtensionAppsBlockForAppServiceInAsh |  | ../chromium/src/ash/constants/ash_switches.cc |
| --launch-rma |  Start Chrome in RMA mode. Launches RMA app automatically.  kRmaNotAllowed switch takes priority over this one. | kLaunchRma |  | ../chromium/src/ash/constants/ash_switches.cc |
| --lobster-feature-key |  Enables the lobster feature. | kLobsterFeatureKey |  | ../chromium/src/ash/constants/ash_switches.cc |
| --login-manager |  Enables Chrome-as-a-login-manager behavior. | kLoginManager |  | ../chromium/src/ash/constants/ash_switches.cc |
| --login-profile |  Specifies the profile to use once a chromeos user is logged in.  This parameter is ignored if user goes through login screen since user_id  hash defines which profile directory to use.  In case of browser restart within active session this parameter is used  to pass user_id hash for primary user. | kLoginProfile |  | ../chromium/src/ash/constants/ash_switches.cc |
| --login-user |  Specifies the user which is already logged in. | kLoginUser |  | ../chromium/src/ash/constants/ash_switches.cc |
| --disallow-lacros |  This flag is set if lacros is not allowed. Specifically this flag is set if  there are more than two signed in users i.e. inside multi-user session. | kDisallowLacros |  | ../chromium/src/ash/constants/ash_switches.cc |
| --disable-disallow-lacros |  This flag disables "disallow-lacros" above, if both are set together.  I.e., if user flips feature flag, or policy is set, lacros can be  used, event if --disallow-lacros is set. | kDisableDisallowLacros |  | ../chromium/src/ash/constants/ash_switches.cc |
| --enable-lacros-for-testing |  This flag is a replacement for  `features::kLacrosOnly` during the in-between phase where users should not be  able to enable Lacros but developers should for debugging. Just like  `features::kLacrosOnly`, passing the flag alone does not guarantee that  Lacros is enabled and other conditions like whether Lacros is allowed to be  enabled i.e. `standalone_browser::BrowserSupport::IsAllowed()` still apply. | kEnableLacrosForTesting |  | ../chromium/src/ash/constants/ash_switches.cc |
| --mahi-feature-key |  Supply secret key for the mahi feature. | kMahiFeatureKey |  | ../chromium/src/ash/constants/ash_switches.cc |
| --sparky-feature-key |  Supply secret key for the sparky feature. | kSparkyFeatureKey |  | ../chromium/src/ash/constants/ash_switches.cc |
| --sparky-server-url |  Supply server url for the sparky feature. | kSparkyServerUrl |  | ../chromium/src/ash/constants/ash_switches.cc |
| --browser-data-migration-for-user |  Specifies the user that the browser data migration should happen for. | kBrowserDataMigrationForUser |  | ../chromium/src/ash/constants/ash_switches.cc |
| --browser-data-backward-migration-for-user |  Specifies the user that the browser data backward migration should happen  for. | kBrowserDataBackwardMigrationForUser |  | ../chromium/src/ash/constants/ash_switches.cc |
| --coral-feature-key |  Supply secret key for Coral feature. | kCoralFeatureKey |  | ../chromium/src/ash/constants/ash_switches.cc |
| --force-browser-data-backward-migration |  Tells Chrome to forcefully trigger backward data migration. | kForceBrowserDataBackwardMigration |  | ../chromium/src/ash/constants/ash_switches.cc |
| --browser-data-migration-mode |  Run move migration instead of copy. Passed with  `kBrowserDataMigrationForUser`. | kBrowserDataMigrationMode |  | ../chromium/src/ash/constants/ash_switches.cc |
| --browser-data-backward-migration-mode |  Backward migration mode. Passed with `kBrowserDataBackwardMigrationForUser`. | kBrowserDataBackwardMigrationMode |  | ../chromium/src/ash/constants/ash_switches.cc |
| --force-browser-data-migration-for-testing |  Force skip or force migration. Should only be used for testing. | kForceBrowserDataMigrationForTesting |  | ../chromium/src/ash/constants/ash_switches.cc |
| --marketing-opt-in-url |  Determines the URL to be used when calling the backend. | kMarketingOptInUrl |  | ../chromium/src/ash/constants/ash_switches.cc |
| --modifier-split-feature-key |  Supply secret key for modifier split feature. | kModifierSplitFeatureKey |  | ../chromium/src/ash/constants/ash_switches.cc |
| --enable-natural-scroll-default |  Enables natural scroll by default. | kNaturalScrollDefault |  | ../chromium/src/ash/constants/ash_switches.cc |
| --note-taking-app-ids |  An optional comma-separated list of IDs of apps that can be used to take  notes. If unset, a hardcoded list is used instead. | kNoteTakingAppIds |  | ../chromium/src/ash/constants/ash_switches.cc |
| --oobe-enable-pin-only-prototype |  Enables a prototype version of the PIN-only OOBE flow. Only for tests.  TODO(b/365059362) - Remove once more stable. | kOobeEnablePinOnlyPrototype |  | ../chromium/src/ash/constants/ash_switches.cc |
| --oobe-eula-url-for-tests |  Allows the eula url to be overridden for tests. | kOobeEulaUrlForTests |  | ../chromium/src/ash/constants/ash_switches.cc |
| --oobe-force-tablet-first-run |  Indicates that the first user run flow (sequence of OOBE screens after the  first user login) should show tablet mode centric screens, even if the device  is not in tablet mode. | kOobeForceTabletFirstRun |  | ../chromium/src/ash/constants/ash_switches.cc |
| --oobe-large-screen-special-scaling |  Indicates that OOBE should be scaled for big displays similar to how Meets  app scales UI.  TODO(crbug.com/1205364): Remove after adding new scheme. | kOobeLargeScreenSpecialScaling |  | ../chromium/src/ash/constants/ash_switches.cc |
| --oobe-print-frontend-load-timings |  When present, prints the time it takes for OOBE's frontend to load.  See go/oobe-frontend-trace-timings for details. | kOobePrintFrontendLoadTimings |  | ../chromium/src/ash/constants/ash_switches.cc |
| --oobe-screenshot-dir |  Specifies directory for screenshots taken with OOBE UI Debugger. | kOobeScreenshotDirectory |  | ../chromium/src/ash/constants/ash_switches.cc |
| --oobe-show-accessibility-button-on-marketing-opt-in-for-testing |  Shows a11y button on the marketing opt in without visiting gesture navigation  screen. | kOobeShowAccessibilityButtonOnMarketingOptInForTesting |  | ../chromium/src/ash/constants/ash_switches.cc |
| --oobe-skip-new-user-check-for-testing |  Skips new user check in the personalized recommend apps screen for testing. | kOobeSkipNewUserCheckForTesting |  | ../chromium/src/ash/constants/ash_switches.cc |
| --oobe-skip-postlogin |  Skips all other OOBE pages after user login. | kOobeSkipPostLogin |  | ../chromium/src/ash/constants/ash_switches.cc |
| --oobe-skip-split-modifier-check-for-testing |  Returns true if we should skip split modifier check on the split modifier  info screen. | kOobeSkipSplitModifierCheckForTesting |  | ../chromium/src/ash/constants/ash_switches.cc |
| --oobe-skip-to-login |  Skip to login screen. | kOobeSkipToLogin |  | ../chromium/src/ash/constants/ash_switches.cc |
| --oobe-timer-interval |  Interval at which we check for total time on OOBE. | kOobeTimerInterval |  | ../chromium/src/ash/constants/ash_switches.cc |
| --oobe-timezone-override-for-tests |  Allows the timezone to be overridden on the marketing opt-in screen. | kOobeTimezoneOverrideForTests |  | ../chromium/src/ash/constants/ash_switches.cc |
| --oobe-trigger-sync-timeout-for-tests |  Trigger sync engine initialization timeout in OOBE for testing. | kOobeTriggerSyncTimeoutForTests |  | ../chromium/src/ash/constants/ash_switches.cc |
| --overview-button-for-tests |  If set, the overview button will be visible. | kOverviewButtonForTests |  | ../chromium/src/ash/constants/ash_switches.cc |
| --hidden-network-migration-interval |  Controls how often the HiddenNetworkHandler class checks for wrongly hidden  networks. The interval should be provided in seconds, should follow the  format "--hidden-network-migration-interval=#", and should be >= 1. | kHiddenNetworkMigrationInterval |  | ../chromium/src/ash/constants/ash_switches.cc |
| --hidden-network-migration-age |  Sets how long a wrongly hidden network must have existed in order to be  considered for removal. The interval should be provided in days, should  follow the format "--hidden-network-migration-age=#", and should be >= 0. | kHiddenNetworkMigrationAge |  | ../chromium/src/ash/constants/ash_switches.cc |
| --picker-feature-key |  | kPickerFeatureKey |  | ../chromium/src/ash/constants/ash_switches.cc |
| --printing-ppd-channel |  Sets the channel from which the PPD files are loaded. | kPrintingPpdChannel |  | ../chromium/src/ash/constants/ash_switches.cc |
| --production |  | kPrintingPpdChannelProduction |  | ../chromium/src/ash/constants/ash_switches.cc |
| --staging |  | kPrintingPpdChannelStaging |  | ../chromium/src/ash/constants/ash_switches.cc |
| --dev |  | kPrintingPpdChannelDev |  | ../chromium/src/ash/constants/ash_switches.cc |
| --localhost |  | kPrintingPpdChannelLocalhost |  | ../chromium/src/ash/constants/ash_switches.cc |
| --privacy-policy-host-for-tests |  Sets Privacy Policy hostname url for testing. | kPrivacyPolicyHostForTests |  | ../chromium/src/ash/constants/ash_switches.cc |
| --profile-requires-policy |  If set to "true", the profile requires policy during restart (policy load  must succeed, otherwise session restart should fail). | kProfileRequiresPolicy |  | ../chromium/src/ash/constants/ash_switches.cc |
| --public-accounts-saml-acl-url |  SAML assertion consumer URL, used to detect when Gaia-less SAML flows end  (e.g. for SAML managed guest sessions)  TODO(crbug.com/40636049): Remove when URL is sent by DMServer. | kPublicAccountsSamlAclUrl |  | ../chromium/src/ash/constants/ash_switches.cc |
| --qs-add-fake-bluetooth-devices |  Adds fake Bluetooth devices to the quick settings menu for UI testing. | kQsAddFakeBluetoothDevices |  | ../chromium/src/ash/constants/ash_switches.cc |
| --qs-add-fake-cast-devices |  Adds fake Cast devices to the quick settings menu for UI testing. | kQsAddFakeCastDevices |  | ../chromium/src/ash/constants/ash_switches.cc |
| --qs-show-locale-tile |  Forces the quick settings "locale" FeatureTile to show. Normally it only  shows in demo mode, which does not work in the emulator. | kQsShowLocaleTile |  | ../chromium/src/ash/constants/ash_switches.cc |
| --regulatory-label-dir |  The name of the per-model directory which contains per-region  subdirectories with regulatory label files for this model.  The per-model directories (if there are any) are located under  "/usr/share/chromeos-assets/regulatory_labels/". | kRegulatoryLabelDir |  | ../chromium/src/ash/constants/ash_switches.cc |
| --remote-reboot-command-timeout-in-seconds-for-testing |  Testing delay for reboot command. Useful for tast tests. | kRemoteRebootCommandDelayInSecondsForTesting |  | ../chromium/src/ash/constants/ash_switches.cc |
| --reven-branding |  Indicates that reven UI strings and features should be shown. | kRevenBranding |  | ../chromium/src/ash/constants/ash_switches.cc |
| --rlz-ping-delay |  The rlz ping delay (in seconds) that overwrites the default value. | kRlzPingDelay |  | ../chromium/src/ash/constants/ash_switches.cc |
| --rma-not-allowed |  Start Chrome without opening RMA or checking the current RMA state. | kRmaNotAllowed |  | ../chromium/src/ash/constants/ash_switches.cc |
| --safe-mode |  The switch added by session_manager daemon when chrome crashes 3 times or  more within the first 60 seconds on start.  See BrowserJob::ExportArgv in platform2/login_manager/browser_job.cc. | kSafeMode |  | ../chromium/src/ash/constants/ash_switches.cc |
| --saml-password-change-url |  Password change url for SAML users.  TODO(crbug.com/40618074): Remove when the bug is fixed. | kSamlPasswordChangeUrl |  | ../chromium/src/ash/constants/ash_switches.cc |
| --shelf-hotseat |  New modular design for the shelf with apps separated into a hotseat UI and  smaller shelf in clamshell mode. | kShelfHotseat |  | ../chromium/src/ash/constants/ash_switches.cc |
| --scanner-update-key |  Supply the secret key for Scanner (for more details see b/363103871). | kScannerUpdateKey |  | ../chromium/src/ash/constants/ash_switches.cc |
| --seal-key |  Supply secret key for Seal feature. | kSealKey |  | ../chromium/src/ash/constants/ash_switches.cc |
| --scheduled-reboot-grace-period-in-seconds-for-testing |  Testing grace period for DeviceScheduledReboot policy. Useful for tast tests.  See `ShouldSkipRebootDueToGracePeriod` in scheduled_task_util.h. | kScheduledRebootGracePeriodInSecondsForTesting |  | ../chromium/src/ash/constants/ash_switches.cc |
| --show-login-dev-overlay |  If true, the developer tool overlay will be shown for the login/lock screen.  This makes it easier to test layout logic. | kShowLoginDevOverlay |  | ../chromium/src/ash/constants/ash_switches.cc |
| --show-oobe-dev-overlay |  Enables OOBE UI Debugger for ease of navigation between screens during manual  testing. Limited to ChromeOS-on-linux and test images only. | kShowOobeDevOverlay |  | ../chromium/src/ash/constants/ash_switches.cc |
| --show-oobe-quick-start-debugger |  Enables the QuickStart debugger in OOBE which mimics an Android phone. | kShowOobeQuickStartDebugger |  | ../chromium/src/ash/constants/ash_switches.cc |
| --show-taps |  Draws a circle at each touch point, similar to the Android OS developer  option "Show taps". | kShowTaps |  | ../chromium/src/ash/constants/ash_switches.cc |
| --skip-force-online-signin-for-testing |  Disables online sign-in enforcement in tast tests. | kSkipForceOnlineSignInForTesting |  | ../chromium/src/ash/constants/ash_switches.cc |
| --skip-multidevice-screen |  Skip multidevice setup screen during tast tests. | kSkipMultideviceScreenForTesting |  | ../chromium/src/ash/constants/ash_switches.cc |
| --skip-reorder-nudge-show-threshold-duration |  Used to skip the threshold duration that the reorder nudge has to show before  the nudge is considered as shown. | kSkipReorderNudgeShowThresholdDurationForTest |  | ../chromium/src/ash/constants/ash_switches.cc |
| --supports-clamshell-auto-rotation |  If set, the device will be forced to stay in clamshell UI mode but screen  auto rotation will be supported. E.g, chromebase device Dooly. | kSupportsClamshellAutoRotation |  | ../chromium/src/ash/constants/ash_switches.cc |
| --suppress-message-center-popups |  Hides all Message Center notification popups (toasts). Used for testing. | kSuppressMessageCenterPopups |  | ../chromium/src/ash/constants/ash_switches.cc |
| --telemetry-extension-dir |  Specifies directory for the Telemetry System Web Extension. | kTelemetryExtensionDirectory |  | ../chromium/src/ash/constants/ash_switches.cc |
| --allow-empty-passwords-in-tests |  TODO(b/299642185): Remove this flag by the end of 2023.  ChromeOS does not support empty passwords for users, but some legacy test  setups might use empty password for users. | kTemporaryAllowEmptyPasswordsInTests |  | ../chromium/src/ash/constants/ash_switches.cc |
| --test-encryption-migration-ui |  Enables testing for encryption migration UI. | kTestEncryptionMigrationUI |  | ../chromium/src/ash/constants/ash_switches.cc |
| --test-wallpaper-server |  Enables the wallpaper picker to fetch images from the test server. | kTestWallpaperServer |  | ../chromium/src/ash/constants/ash_switches.cc |
| --tether-host-scans-ignore-wired-connections |  Tells the Chromebook to scan for a tethering host even if there is already a  wired connection. This allows end-to-end tests to be deployed over ethernet  without that connection preventing scans and thereby blocking the testing of  cases with no preexisting connection. Should be used only for testing. | kTetherHostScansIgnoreWiredConnections |  | ../chromium/src/ash/constants/ash_switches.cc |
| --tether-stub |  Overrides Tether with stub service. Provide integer arguments for the number  of fake networks desired, e.g. 'tether-stub=2'. | kTetherStub |  | ../chromium/src/ash/constants/ash_switches.cc |
| --time-before-onboarding-survey-in-seconds-for-testing |  Used for overriding the required user activity time before running the  onboarding survey. | kTimeBeforeOnboardingSurveyInSecondsForTesting |  | ../chromium/src/ash/constants/ash_switches.cc |
| --touchscreen-usable-while-screen-off |  Chromebases' touchscreens can be used to wake from suspend, unlike the  touchscreens on other Chrome OS devices. If set, the touchscreen is kept  enabled while the screen is off so that it can be used to turn the screen  back on after it has been turned off for inactivity but before the system has  suspended. | kTouchscreenUsableWhileScreenOff |  | ../chromium/src/ash/constants/ash_switches.cc |
| --tpm-is-dynamic |  Enables TPM selection in runtime. | kTpmIsDynamic |  | ../chromium/src/ash/constants/ash_switches.cc |
| --unfiltered-bluetooth-devices |  Shows all Bluetooth devices in UI (System Tray/Settings Page.) | kUnfilteredBluetoothDevices |  | ../chromium/src/ash/constants/ash_switches.cc |
| --aue-reached-for-update-required-test |  If this switch is passed, the device policy DeviceMinimumVersion  assumes that the device has reached Auto Update Expiration. This is useful  for testing the policy behaviour on the DUT. | kUpdateRequiredAueForTest |  | ../chromium/src/ash/constants/ash_switches.cc |
| --use-fake-cras-audio-client-for-dbus |  Use the fake FakeCrasAudioClient to handle system audio controls. | kUseFakeCrasAudioClientForDBus |  | ../chromium/src/ash/constants/ash_switches.cc |
| --use-myfiles-in-user-data-dir-for-testing |  Flag that stored MyFiles folder inside the user data directory.  $HOME/Downloads is used as MyFiles folder for ease access to local files for  debugging when running on Linux. By setting this flag, <cryptohome>/MyFiles  is used even on Linux. | kUseMyFilesInUserDataDirForTesting |  | ../chromium/src/ash/constants/ash_switches.cc |
| --web-ui-data-source-path-for-testing |  If provided, any webui will be loaded from <flag value>/<handler_name>, where  handler_name is the name passed to MaybeConfigureTestableDataSource, if the  file exists.  For example, if the flag is /tmp/resource_overrides, attempting to load  js/app_main.js from the data source named "help_app/untrusted" will first  attempt to load from /tmp/resource_overrides/help_app/untrusted/js/main.js. | kWebUiDataSourcePathForTesting |  | ../chromium/src/ash/constants/ash_switches.cc |
| --get-access-token-for-test |  Enable the getAccessToken autotest API which creates access tokens using  the internal OAuth client ID. | kGetAccessTokenForTest |  | ../chromium/src/ash/constants/ash_switches.cc |
| --prevent-kiosk-autolaunch-for-testing |  Prevent kiosk autolaunch for testing. | kPreventKioskAutolaunchForTesting |  | ../chromium/src/ash/constants/ash_switches.cc |
| --ash-allow-default-shelf-pin-layout-ignoring-sync |  Allows the Ash shelf to apply the default pin layout without waiting for Sync  to download data from the server (which many tests can't achieve). | kAllowDefaultShelfPinLayoutIgnoringSync |  | ../chromium/src/ash/constants/ash_switches.cc |
| --force-refresh-rate-throttle |  On devices that support refresh rate throttling, force the throttling  behavior to be active regardless of system state. | kForceRefreshRateThrottle |  | ../chromium/src/ash/constants/ash_switches.cc |
| switch | description | variable | cpp condition | location |
| ------ | ----------- | -------- | ------------- | -------- |
| switch | description | variable | cpp condition | location |
| ------ | ----------- | -------- | ------------- | -------- |
| switch | description | variable | cpp condition | location |
| ------ | ----------- | -------- | ------------- | -------- |
| switch | description | variable | cpp condition | location |
| ------ | ----------- | -------- | ------------- | -------- |
| switch | description | variable | cpp condition | location |
| ------ | ----------- | -------- | ------------- | -------- |
| switch | description | variable | cpp condition | location |
| ------ | ----------- | -------- | ------------- | -------- |
| switch | description | variable | cpp condition | location |
| ------ | ----------- | -------- | ------------- | -------- |
| switch | description | variable | cpp condition | location |
| ------ | ----------- | -------- | ------------- | -------- |
| switch | description | variable | cpp condition | location |
| ------ | ----------- | -------- | ------------- | -------- |
| switch | description | variable | cpp condition | location |
| ------ | ----------- | -------- | ------------- | -------- |
| --enable-virtual-keyboard |  | kEnableVirtualKeyboard |  | ../chromium/src/ash/public/cpp/keyboard/keyboard_switches.cc |
| --disable-virtual-keyboard |  | kDisableVirtualKeyboard |  | ../chromium/src/ash/public/cpp/keyboard/keyboard_switches.cc |
| switch | description | variable | cpp condition | location |
| ------ | ----------- | -------- | ------------- | -------- |
| switch | description | variable | cpp condition | location |
| ------ | ----------- | -------- | ------------- | -------- |
| switch | description | variable | cpp condition | location |
| ------ | ----------- | -------- | ------------- | -------- |
| switch | description | variable | cpp condition | location |
| ------ | ----------- | -------- | ------------- | -------- |
| switch | description | variable | cpp condition | location |
| ------ | ----------- | -------- | ------------- | -------- |
| switch | description | variable | cpp condition | location |
| ------ | ----------- | -------- | ------------- | -------- |
| switch | description | variable | cpp condition | location |
| ------ | ----------- | -------- | ------------- | -------- |
| switch | description | variable | cpp condition | location |
| ------ | ----------- | -------- | ------------- | -------- |
| switch | description | variable | cpp condition | location |
| ------ | ----------- | -------- | ------------- | -------- |
| switch | description | variable | cpp condition | location |
| ------ | ----------- | -------- | ------------- | -------- |
| switch | description | variable | cpp condition | location |
| ------ | ----------- | -------- | ------------- | -------- |
| switch | description | variable | cpp condition | location |
| ------ | ----------- | -------- | ------------- | -------- |
| switch | description | variable | cpp condition | location |
| ------ | ----------- | -------- | ------------- | -------- |
| switch | description | variable | cpp condition | location |
| ------ | ----------- | -------- | ------------- | -------- |
| switch | description | variable | cpp condition | location |
| ------ | ----------- | -------- | ------------- | -------- |
| switch | description | variable | cpp condition | location |
| ------ | ----------- | -------- | ------------- | -------- |
| switch | description | variable | cpp condition | location |
| ------ | ----------- | -------- | ------------- | -------- |
| switch | description | variable | cpp condition | location |
| ------ | ----------- | -------- | ------------- | -------- |
| switch | description | variable | cpp condition | location |
| ------ | ----------- | -------- | ------------- | -------- |
| switch | description | variable | cpp condition | location |
| ------ | ----------- | -------- | ------------- | -------- |
| switch | description | variable | cpp condition | location |
| ------ | ----------- | -------- | ------------- | -------- |
| switch | description | variable | cpp condition | location |
| ------ | ----------- | -------- | ------------- | -------- |
| switch | description | variable | cpp condition | location |
| ------ | ----------- | -------- | ------------- | -------- |
| --disable-best-effort-tasks |  Delays execution of TaskPriority::BEST_EFFORT tasks until shutdown. | kDisableBestEffortTasks |  | ../chromium/src/base/base_switches.cc |
| --disable-breakpad |  Disables the crash reporting. | kDisableBreakpad |  | ../chromium/src/base/base_switches.cc |
| --disable-features |  Comma-separated list of feature names to disable. See also kEnableFeatures. | kDisableFeatures |  | ../chromium/src/base/base_switches.cc |
| --disable-low-end-device-mode |  Force disabling of low-end device mode when set. | kDisableLowEndDeviceMode |  | ../chromium/src/base/base_switches.cc |
| --enable-crash-reporter |  Indicates that crash reporting should be enabled. On platforms where helper  processes cannot access to files needed to make this decision, this flag is  generated internally. | kEnableCrashReporter |  | ../chromium/src/base/base_switches.cc |
| --enable-features |  Comma-separated list of feature names to enable. See also kDisableFeatures. | kEnableFeatures |  | ../chromium/src/base/base_switches.cc |
| --enable-low-end-device-mode |  Force low-end device mode when set. | kEnableLowEndDeviceMode |  | ../chromium/src/base/base_switches.cc |
| --enable-background-thread-pool |  Enable the use of background thread priorities for background tasks in the  ThreadPool even on systems where it is disabled by default, e.g. due to  concerns about priority inversions. | kEnableBackgroundThreadPool |  | ../chromium/src/base/base_switches.cc |
| --field-trial-handle |  Handle to the shared memory segment containing field trial state that is to  be shared between processes. The argument to this switch is made of segments  separated by commas:  - The platform-specific handle id for the shared memory as a string.  - (Windows only) i=inherited by duplication or p=child must open parent.  - The high 64 bits of the shared memory block GUID.  - The low 64 bits of the shared memory block GUID.  - The size of the shared memory segment as a string. | kFieldTrialHandle |  | ../chromium/src/base/base_switches.cc |
| --force-fieldtrials |  This option can be used to force field trials when testing changes locally.  The argument is a list of name and value pairs, separated by slashes. If a  trial name is prefixed with an asterisk, that trial will start activated.  For example, the following argument defines two trials, with the second one  activated: "GoogleNow/Enable/*MaterialDesignNTP/Default/" This option can  also be used by the browser process to send the list of trials to a  non-browser process, using the same format. See  FieldTrialList::CreateTrialsFromString() in field_trial.h for details. | kForceFieldTrials |  | ../chromium/src/base/base_switches.cc |
| --full-memory-crash-report |  Generates full memory crash dump. | kFullMemoryCrashReport |  | ../chromium/src/base/base_switches.cc |
| --log-best-effort-tasks |  Logs information about all tasks posted with TaskPriority::BEST_EFFORT. Use  this to diagnose issues that are thought to be caused by  TaskPriority::BEST_EFFORT execution fences. Note: Tasks posted to a  non-BEST_EFFORT UpdateableSequencedTaskRunner whose priority is later lowered  to BEST_EFFORT are not logged. | kLogBestEffortTasks |  | ../chromium/src/base/base_switches.cc |
| --metrics-shmem-handle |  Handle to the shared memory segment a child process should use to transmit  histograms back to the browser process. | kMetricsSharedMemoryHandle |  | ../chromium/src/base/base_switches.cc |
| --noerrdialogs |  Suppresses all error dialogs when present. | kNoErrorDialogs |  | ../chromium/src/base/base_switches.cc |
| --profiling-at-start |  Starts the sampling based profiler for the browser process at startup. This  will only work if chrome has been built with the gn arg enable_profiling =  true. The output will go to the value of kProfilingFile. | kProfilingAtStart |  | ../chromium/src/base/base_switches.cc |
| --profiling-file |  Specifies a location for profiling output. This will only work if chrome has  been built with the gyp variable profiling=1 or gn arg enable_profiling=true.     {pid} if present will be replaced by the pid of the process.    {count} if present will be incremented each time a profile is generated            for this process.  The default is chrome-profile-{pid} for the browser and test-profile-{pid}  for tests. | kProfilingFile |  | ../chromium/src/base/base_switches.cc |
| --profiling-flush |  Controls whether profile data is periodically flushed to a file. Normally  the data gets written on exit but cases exist where chromium doesn't exit  cleanly (especially when using single-process). A time in seconds can be  specified. | kProfilingFlush |  | ../chromium/src/base/base_switches.cc |
| --test-child-process |  When running certain tests that spawn child processes, this switch indicates  to the test framework that the current process is a child process. | kTestChildProcess |  | ../chromium/src/base/base_switches.cc |
| --trace-to-file |  Sends trace events from these categories to a file.  --trace-to-file on its own sends to default categories. | kTraceToFile |  | ../chromium/src/base/base_switches.cc |
| --trace-to-file-name |  Specifies the file name for --trace-to-file. If unspecified, it will  go to a default file name. | kTraceToFileName |  | ../chromium/src/base/base_switches.cc |
| --v |  Gives the default maximal active V-logging level; 0 is the default.  Normally positive values are used for V-logging levels. | kV |  | ../chromium/src/base/base_switches.cc |
| --vmodule |  Gives the per-module maximal V-logging levels to override the value  given by --v.  E.g. "my_module=2,foo*=3" would change the logging  level for all code in source files "my_module.*" and "foo*.*"  ("-inl" suffixes are also disregarded for this matching).   Any pattern containing a forward or backward slash will be tested  against the whole pathname and not just the module.  E.g.,  "*/foo/bar/*=2" would change the logging level for all code in  source files under a "foo/bar" directory. | kVModule |  | ../chromium/src/base/base_switches.cc |
| --wait-for-debugger |  Will wait for 60 seconds for a debugger to come to attach to the process. | kWaitForDebugger |  | ../chromium/src/base/base_switches.cc |
| --disable-highres-timer |  Disable high-resolution timer on Windows. | kDisableHighResTimer | BUILDFLAG(IS_WIN) | ../chromium/src/base/base_switches.cc |
| --disable-usb-keyboard-detect |  Disables the USB keyboard detection for blocking the OSK on Windows. | kDisableUsbKeyboardDetect | BUILDFLAG(IS_WIN) | ../chromium/src/base/base_switches.cc |
| --disable-dev-shm-usage |  The /dev/shm partition is too small in certain VM environments, causing  Chrome to fail or crash (see http:crbug.com/715363). Use this flag to  work-around this issue (a temporary directory will always be used to create  anonymous shared memory files). | kDisableDevShmUsage | BUILDFLAG(IS_LINUX) | ../chromium/src/base/base_switches.cc |
| --enable-crash-reporter-for-testing |  Used for turning on Breakpad crash reporting in a debug environment where  crash reporting is typically compiled but disabled. | kEnableCrashReporterForTesting | BUILDFLAG(IS_POSIX) | ../chromium/src/base/base_switches.cc |
| --default-country-code |  Default country code to be used for search engine localization. | kDefaultCountryCodeAtInstall | BUILDFLAG(IS_ANDROID) | ../chromium/src/base/base_switches.cc |
| --enable-idle-tracing |  Adds additional thread idle time information into the trace event output. | kEnableIdleTracing | BUILDFLAG(IS_ANDROID) | ../chromium/src/base/base_switches.cc |
| --force-fieldtrial-params |  The field trial parameters and their values when testing changes locally. | kForceFieldTrialParams | BUILDFLAG(IS_ANDROID) | ../chromium/src/base/base_switches.cc |
| --host-package-name |  When we retrieve the package name within the SDK Runtime, we need to use  a bit of a hack to do this by taking advantage of the fact that the pid  is the same pid as the application's pid + 10000.  see:  https:cs.android.com/android/platform/superproject/main/+/main:frameworks/base/core/java/android/os/Process.java;l=292;drc=47fffdd53115a9af1820e3f89d8108745be4b55d  When the render process is created however, it is just a regular isolated  process with no particular association so we can't perform the same hack.  When creating minidumps, the package name is retrieved from the process  meaning the render process minidumps would end up reporting a generic  process name not associated with the app.  We work around this by feeding through the host package information to the  render process when launching it. | kHostPackageName | BUILDFLAG(IS_ANDROID) | ../chromium/src/base/base_switches.cc |
| --host-package-label |  | kHostPackageLabel | BUILDFLAG(IS_ANDROID) | ../chromium/src/base/base_switches.cc |
| --host-version-code |  | kHostVersionCode | BUILDFLAG(IS_ANDROID) | ../chromium/src/base/base_switches.cc |
| --package-name |  | kPackageName | BUILDFLAG(IS_ANDROID) | ../chromium/src/base/base_switches.cc |
| --package-version-name |  | kPackageVersionName | BUILDFLAG(IS_ANDROID) | ../chromium/src/base/base_switches.cc |
| --scheduler-boost-urgent |  Override the default scheduling boosting value for urgent tasks.  This can be adjusted if a specific chromeos device shows better perf/power  ratio (e.g. by running video conference tests).  Currently, this values directs to linux scheduler's utilization min clamp.  Range is 0(no biased load) ~ 100(mamximum load value). | kSchedulerBoostUrgent | BUILDFLAG(IS_CHROMEOS) | ../chromium/src/base/base_switches.cc |
| switch | description | variable | cpp condition | location |
| ------ | ----------- | -------- | ------------- | -------- |
| --force-ui-direction |  Force the UI to a specific direction. Valid values are "ltr" (left-to-right)  and "rtl" (right-to-left). | kForceUIDirection |  | ../chromium/src/base/i18n/base_i18n_switches.cc |
| --force-text-direction |  Force the text rendering to a specific direction. Valid values are "ltr"  (left-to-right) and "rtl" (right-to-left). Only tested meaningfully with  RTL. | kForceTextDirection |  | ../chromium/src/base/i18n/base_i18n_switches.cc |
| --ltr |  | kForceDirectionLTR |  | ../chromium/src/base/i18n/base_i18n_switches.cc |
| --rtl |  | kForceDirectionRTL |  | ../chromium/src/base/i18n/base_i18n_switches.cc |
| switch | description | variable | cpp condition | location |
| ------ | ----------- | -------- | ------------- | -------- |
| switch | description | variable | cpp condition | location |
| ------ | ----------- | -------- | ------------- | -------- |
| switch | description | variable | cpp condition | location |
| ------ | ----------- | -------- | ------------- | -------- |
| switch | description | variable | cpp condition | location |
| ------ | ----------- | -------- | ------------- | -------- |
| --disable-threaded-animation |  | kDisableThreadedAnimation |  | ../chromium/src/cc/base/switches.cc |
| --disable-composited-antialiasing |  Disables layer-edge anti-aliasing in the compositor. | kDisableCompositedAntialiasing |  | ../chromium/src/cc/base/switches.cc |
| --disable-main-frame-before-activation |  Disables sending the next BeginMainFrame before the previous commit  activates. Overrides the kEnableMainFrameBeforeActivation flag. | kDisableMainFrameBeforeActivation |  | ../chromium/src/cc/base/switches.cc |
| --enable-main-frame-before-activation |  Enables sending the next BeginMainFrame before the previous commit activates. | kEnableMainFrameBeforeActivation |  | ../chromium/src/cc/base/switches.cc |
| --disable-checker-imaging |  Disabled defering all image decodes to the image decode service, ignoring  DecodingMode preferences specified on PaintImage. | kDisableCheckerImaging |  | ../chromium/src/cc/base/switches.cc |
| --top-controls-hide-threshold |  Percentage of the browser controls need to be hidden before they will auto  hide. | kBrowserControlsHideThreshold |  | ../chromium/src/cc/base/switches.cc |
| --top-controls-show-threshold |  Percentage of the browser controls need to be shown before they will auto  show. | kBrowserControlsShowThreshold |  | ../chromium/src/cc/base/switches.cc |
| --slow-down-raster-scale-factor |  Re-rasters everything multiple times to simulate a much slower machine.  Give a scale factor to cause raster to take that many times longer to  complete, such as --slow-down-raster-scale-factor=25. | kSlowDownRasterScaleFactor |  | ../chromium/src/cc/base/switches.cc |
| --check-damage-early |  Checks damage early and aborts the frame if no damage, so that clients like  Android WebView don't invalidate unnecessarily. | kCheckDamageEarly |  | ../chromium/src/cc/base/switches.cc |
| --enable-gpu-benchmarking |  Enables the GPU benchmarking extension | kEnableGpuBenchmarking |  | ../chromium/src/cc/base/switches.cc |
| --disable-layer-tree-host-memory-pressure |  Disables LayerTreeHost::OnMemoryPressure | kDisableLayerTreeHostMemoryPressure |  | ../chromium/src/cc/base/switches.cc |
| --num-raster-threads |  Controls the number of threads to use for raster tasks. | kNumRasterThreads |  | ../chromium/src/cc/base/switches.cc |
| --show-composited-layer-borders |  Renders a border around compositor layers to help debug and study  layer compositing. | kShowCompositedLayerBorders |  | ../chromium/src/cc/base/switches.cc |
| --ui-show-composited-layer-borders |  | kUIShowCompositedLayerBorders |  | ../chromium/src/cc/base/switches.cc |
| --renderpass |  Parameters for kUIShowCompositedLayerBorders. | kCompositedRenderPassBorders |  | ../chromium/src/cc/base/switches.cc |
| --surface |  | kCompositedSurfaceBorders |  | ../chromium/src/cc/base/switches.cc |
| --layer |  | kCompositedLayerBorders |  | ../chromium/src/cc/base/switches.cc |
| --log-on-ui-double-background-blur |  Checks and logs double background blur as an error if any. | kLogOnUIDoubleBackgroundBlur | DCHECK_IS_ON() | ../chromium/src/cc/base/switches.cc |
| --show-fps-counter |  Draws a heads-up-display showing Frames Per Second as well as GPU memory  usage. If you also use --enable-logging=stderr --vmodule="head*=1" then FPS  will also be output to the console log. | kShowFPSCounter |  | ../chromium/src/cc/base/switches.cc |
| --ui-show-fps-counter |  | kUIShowFPSCounter |  | ../chromium/src/cc/base/switches.cc |
| --show-layer-animation-bounds |  Renders a border that represents the bounding box for the layer's animation. | kShowLayerAnimationBounds |  | ../chromium/src/cc/base/switches.cc |
| --ui-show-layer-animation-bounds |  | kUIShowLayerAnimationBounds |  | ../chromium/src/cc/base/switches.cc |
| --show-property-changed-rects |  Show rects in the HUD around layers whose properties have changed. | kShowPropertyChangedRects |  | ../chromium/src/cc/base/switches.cc |
| --ui-show-property-changed-rects |  | kUIShowPropertyChangedRects |  | ../chromium/src/cc/base/switches.cc |
| --show-surface-damage-rects |  Show rects in the HUD around damage as it is recorded into each render  surface. | kShowSurfaceDamageRects |  | ../chromium/src/cc/base/switches.cc |
| --ui-show-surface-damage-rects |  | kUIShowSurfaceDamageRects |  | ../chromium/src/cc/base/switches.cc |
| --show-screenspace-rects |  Show rects in the HUD around the screen-space transformed bounds of every  layer. | kShowScreenSpaceRects |  | ../chromium/src/cc/base/switches.cc |
| --ui-show-screenspace-rects |  | kUIShowScreenSpaceRects |  | ../chromium/src/cc/base/switches.cc |
| --highlight-non-lcd-text-layers |  Highlights layers that can't use lcd text. Layers containing no text won't  be highlighted. See DebugColors::NonLCDTextHighlightColor() for the colors. | kHighlightNonLCDTextLayers |  | ../chromium/src/cc/base/switches.cc |
| --animated-image-resume |  Enables the resume method on animated images. | kAnimatedImageResume |  | ../chromium/src/cc/base/switches.cc |
| --enable-scaling-clipped-images |  Allows scaling clipped images in GpuImageDecodeCache. Note that this may  cause color-bleeding.  TODO(crbug.com/40160880): Remove this workaround flag once the underlying  cache problems are solved. | kEnableClippedImageScaling |  | ../chromium/src/cc/base/switches.cc |
| --cc-layer-tree-test-no-timeout |  Prevents the layer tree unit tests from timing out. | kCCLayerTreeTestNoTimeout |  | ../chromium/src/cc/base/switches.cc |
| --cc-layer-tree-test-long-timeout |  Increases timeout for memory checkers. | kCCLayerTreeTestLongTimeout |  | ../chromium/src/cc/base/switches.cc |
| --cc-scroll-animation-duration-in-seconds |  Controls the duration of the scroll animation curve. | kCCScrollAnimationDurationForTesting |  | ../chromium/src/cc/base/switches.cc |
| switch | description | variable | cpp condition | location |
| ------ | ----------- | -------- | ------------- | -------- |
| switch | description | variable | cpp condition | location |
| ------ | ----------- | -------- | ------------- | -------- |
| switch | description | variable | cpp condition | location |
| ------ | ----------- | -------- | ------------- | -------- |
| --custom-android-messages-domain |  | kCustomAndroidMessagesDomain |  | ../chromium/src/chrome/browser/ash/android_sms/android_sms_switches.cc |
| switch | description | variable | cpp condition | location |
| ------ | ----------- | -------- | ------------- | -------- |
| switch | description | variable | cpp condition | location |
| ------ | ----------- | -------- | ------------- | -------- |
| switch | description | variable | cpp condition | location |
| ------ | ----------- | -------- | ------------- | -------- |
| --borealis-launch-options |  Allows passing a BorealisLaunchOptions string to the chrome process, which  will be stored in the kExtraLaunchOptions. For the format, see the  documentation in chrome/browser/ash/borealis/borealis_launch_options.h. | kLaunchOptions |  | ../chromium/src/chrome/browser/ash/borealis/borealis_switches.cc |
| switch | description | variable | cpp condition | location |
| ------ | ----------- | -------- | ------------- | -------- |
| switch | description | variable | cpp condition | location |
| ------ | ----------- | -------- | ------------- | -------- |
| switch | description | variable | cpp condition | location |
| ------ | ----------- | -------- | ------------- | -------- |
| switch | description | variable | cpp condition | location |
| ------ | ----------- | -------- | ------------- | -------- |
| switch | description | variable | cpp condition | location |
| ------ | ----------- | -------- | ------------- | -------- |
| switch | description | variable | cpp condition | location |
| ------ | ----------- | -------- | ------------- | -------- |
| switch | description | variable | cpp condition | location |
| ------ | ----------- | -------- | ------------- | -------- |
| switch | description | variable | cpp condition | location |
| ------ | ----------- | -------- | ------------- | -------- |
| switch | description | variable | cpp condition | location |
| ------ | ----------- | -------- | ------------- | -------- |
| switch | description | variable | cpp condition | location |
| ------ | ----------- | -------- | ------------- | -------- |
| --heildphpnddilhkemkielfhnkaagiabh |  namespace | kLBSExtensionId |  | ../chromium/src/chrome/browser/browser_switcher/browser_switcher_policy_migrator.cc |
| switch | description | variable | cpp condition | location |
| ------ | ----------- | -------- | ------------- | -------- |
| switch | description | variable | cpp condition | location |
| ------ | ----------- | -------- | ------------- | -------- |
| switch | description | variable | cpp condition | location |
| ------ | ----------- | -------- | ------------- | -------- |
| switch | description | variable | cpp condition | location |
| ------ | ----------- | -------- | ------------- | -------- |
| switch | description | variable | cpp condition | location |
| ------ | ----------- | -------- | ------------- | -------- |
| switch | description | variable | cpp condition | location |
| ------ | ----------- | -------- | ------------- | -------- |
| switch | description | variable | cpp condition | location |
| ------ | ----------- | -------- | ------------- | -------- |
| switch | description | variable | cpp condition | location |
| ------ | ----------- | -------- | ------------- | -------- |
| switch | description | variable | cpp condition | location |
| ------ | ----------- | -------- | ------------- | -------- |
| --use-va-dev-keys |  | kUseVaDevKeys |  | ../chromium/src/chrome/browser/enterprise/connectors/device_trust/attestation/browser/attestation_switches.cc |
| switch | description | variable | cpp condition | location |
| ------ | ----------- | -------- | ------------- | -------- |
| switch | description | variable | cpp condition | location |
| ------ | ----------- | -------- | ------------- | -------- |
| switch | description | variable | cpp condition | location |
| ------ | ----------- | -------- | ------------- | -------- |
| --simulate-update-hresult |  Simulates a specific HRESULT error code returned by the update check.  If the switch value is not specified (as hex) then it defaults to E_FAIL. | kSimulateUpdateHresult |  | ../chromium/src/chrome/browser/google/switches.cc |
| --simulate-update-error-code |  Simulates a GoogleUpdateErrorCode error by the update check.  Must be supplied with |kSimulateUpdateHresult| switch. | kSimulateUpdateErrorCode |  | ../chromium/src/chrome/browser/google/switches.cc |
| switch | description | variable | cpp condition | location |
| ------ | ----------- | -------- | ------------- | -------- |
| --disable-ip-privacy-proxy |  | kDisableIpProtectionProxy |  | ../chromium/src/chrome/browser/ip_protection/ip_protection_switches.cc |
| switch | description | variable | cpp condition | location |
| ------ | ----------- | -------- | ------------- | -------- |
| switch | description | variable | cpp condition | location |
| ------ | ----------- | -------- | ------------- | -------- |
| switch | description | variable | cpp condition | location |
| ------ | ----------- | -------- | ------------- | -------- |
| --nearby-share-certificate-validity-period-hours |  Overrides the default validity period for Nearby Share certificates. Value  must be larger than 0. | kNearbyShareCertificateValidityPeriodHours |  | ../chromium/src/chrome/browser/nearby_sharing/common/nearby_share_switches.cc |
| --nearby-share-device-id |  Overrides the default device ID to provide a stable ID in test environments.  By default we generate a random 10-character string. | kNearbyShareDeviceID |  | ../chromium/src/chrome/browser/nearby_sharing/common/nearby_share_switches.cc |
| --nearbysharing-http-host |  Overrides the default URL for Google APIs (https:www.googleapis.com) used  by Nearby Share | kNearbyShareHTTPHost |  | ../chromium/src/chrome/browser/nearby_sharing/common/nearby_share_switches.cc |
| --nearby-share-num-private-certificates |  Overrides the default number of private certificates generated. Value must be  larger than 0. | kNearbyShareNumPrivateCertificates |  | ../chromium/src/chrome/browser/nearby_sharing/common/nearby_share_switches.cc |
| --nearby-share-verbose-logging |  Enables verbose logging level for Nearby Share. | kNearbyShareVerboseLogging |  | ../chromium/src/chrome/browser/nearby_sharing/common/nearby_share_switches.cc |
| switch | description | variable | cpp condition | location |
| ------ | ----------- | -------- | ------------- | -------- |
| switch | description | variable | cpp condition | location |
| ------ | ----------- | -------- | ------------- | -------- |
| --signed-out-ntp-modules |  | kSignedOutNtpModulesSwitch |  | ../chromium/src/chrome/browser/new_tab_page/modules/modules_switches.cc |
| switch | description | variable | cpp condition | location |
| ------ | ----------- | -------- | ------------- | -------- |
| switch | description | variable | cpp condition | location |
| ------ | ----------- | -------- | ------------- | -------- |
| switch | description | variable | cpp condition | location |
| ------ | ----------- | -------- | ------------- | -------- |
| --loading-predictor-allow-local-request-for-testing |  Allows the loading predictor to do prefetches to local IP addresses. This is  needed for testing as such requests are blocked by default for security. | kLoadingPredictorAllowLocalRequestForTesting |  | ../chromium/src/chrome/browser/predictors/predictors_switches.cc |
| switch | description | variable | cpp condition | location |
| ------ | ----------- | -------- | ------------- | -------- |
| switch | description | variable | cpp condition | location |
| ------ | ----------- | -------- | ------------- | -------- |
| switch | description | variable | cpp condition | location |
| ------ | ----------- | -------- | ------------- | -------- |
| switch | description | variable | cpp condition | location |
| ------ | ----------- | -------- | ------------- | -------- |
| switch | description | variable | cpp condition | location |
| ------ | ----------- | -------- | ------------- | -------- |
| switch | description | variable | cpp condition | location |
| ------ | ----------- | -------- | ------------- | -------- |
| switch | description | variable | cpp condition | location |
| ------ | ----------- | -------- | ------------- | -------- |
| switch | description | variable | cpp condition | location |
| ------ | ----------- | -------- | ------------- | -------- |
| --webauthn-remote-proxied-requests-allowed-additional-origin |  | kRemoteProxiedRequestsAllowedAdditionalOrigin |  | ../chromium/src/chrome/browser/webauthn/webauthn_switches.cc |
| --webauthn-permit-enterprise-attestation |  | kPermitEnterpriseAttestationOriginList |  | ../chromium/src/chrome/browser/webauthn/webauthn_switches.cc |
| --webauthn-gpm-pin-reset-reauth-url |  | kGpmPinResetReauthUrlSwitch |  | ../chromium/src/chrome/browser/webauthn/webauthn_switches.cc |
| switch | description | variable | cpp condition | location |
| ------ | ----------- | -------- | ------------- | -------- |
| --accept-lang |  -----------------------------------------------------------------------------  Can't find the switch you are looking for? Try looking in:  ash/constants/ash_switches.cc  base/base_switches.cc  etc.   When commenting your switch, please use the same voice as surrounding  comments. Imagine "This switch..." at the beginning of the phrase, and it'll  all work out.  -----------------------------------------------------------------------------  Specifies Accept-Language to send to servers and expose to JavaScript via the  navigator.language DOM property. language[-country] where language is the 2  letter code from ISO-639. | kAcceptLang |  | ../chromium/src/chrome/common/chrome_switches.cc |
| --allow-cross-origin-auth-prompt |  Allows third-party content included on a page to prompt for a HTTP basic  auth username/password pair. | kAllowCrossOriginAuthPrompt |  | ../chromium/src/chrome/common/chrome_switches.cc |
| --allow-http-screen-capture |  Allow non-secure origins to use the screen capture API and the desktopCapture  extension API. | kAllowHttpScreenCapture |  | ../chromium/src/chrome/common/chrome_switches.cc |
| --allow-running-insecure-content |  By default, an https page cannot run JavaScript, CSS or plugins from http  URLs. This provides an override to get the old insecure behavior. | kAllowRunningInsecureContent |  | ../chromium/src/chrome/common/chrome_switches.cc |
| --allow-silent-push |  Allows Web Push notifications that do not show a notification. | kAllowSilentPush |  | ../chromium/src/chrome/common/chrome_switches.cc |
| --app |  Specifies that the associated value should be launched in "application"  mode. | kApp |  | ../chromium/src/chrome/common/chrome_switches.cc |
| --app-id |  Specifies that the extension-app with the specified id should be launched  according to its configuration. | kAppId |  | ../chromium/src/chrome/common/chrome_switches.cc |
| --app-launch-url-for-shortcuts-menu-item |  Overrides the launch url of an app with the specified url. This is used  along with kAppId to launch a given app with the url corresponding to an item  in the app's shortcuts menu. | kAppLaunchUrlForShortcutsMenuItem |  | ../chromium/src/chrome/common/chrome_switches.cc |
| --app-mode-auth-code |  Value of GAIA auth code for --force-app-mode. | kAppModeAuthCode |  | ../chromium/src/chrome/common/chrome_switches.cc |
| --app-mode-oauth-token |  Value of OAuth2 refresh token for --force-app-mode. | kAppModeOAuth2Token |  | ../chromium/src/chrome/common/chrome_switches.cc |
| --app-run-on-os-login-mode |  This is used along with kAppId to indicate an app was launched during  OS login, and which mode the app was launched in. | kAppRunOnOsLoginMode |  | ../chromium/src/chrome/common/chrome_switches.cc |
| --apps-gallery-download-url |  Overrides the URL that the webstore APIs download extensions from.  Note: the URL must contain one '%s' for the extension ID. | kAppsGalleryDownloadURL |  | ../chromium/src/chrome/common/chrome_switches.cc |
| --apps-gallery-update-url |  Overrides the update url used by webstore extensions. | kAppsGalleryUpdateURL |  | ../chromium/src/chrome/common/chrome_switches.cc |
| --apps-gallery-url |  Overrides the url that the browser treats as the webstore, granting it the  webstore APIs and giving it some special protections. | kAppsGalleryURL |  | ../chromium/src/chrome/common/chrome_switches.cc |
| --auth-server-allowlist |  Allowlist for Negotiate Auth servers | kAuthServerAllowlist |  | ../chromium/src/chrome/common/chrome_switches.cc |
| --auto-open-devtools-for-tabs |  This flag makes Chrome auto-open DevTools window for each tab. It is  intended to be used by developers and automation to not require user  interaction for opening DevTools. | kAutoOpenDevToolsForTabs |  | ../chromium/src/chrome/common/chrome_switches.cc |
| --auto-select-desktop-capture-source |  This flag makes Chrome auto-select the provided choice when an extension asks  permission to start desktop capture. Should only be used for tests. For  instance, --auto-select-desktop-capture-source="Entire screen" will  automatically select sharing the entire screen in English locales. The switch  value only needs to be substring of the capture source name, i.e. "display"  would match "Built-in display" and "External display", whichever comes first. | kAutoSelectDesktopCaptureSource |  | ../chromium/src/chrome/common/chrome_switches.cc |
| --auto-select-tab-capture-source-by-title |  This flag makes Chrome auto-select a tab with the provided title when  the media-picker should otherwise be displayed to the user. This switch  is very similar to kAutoSelectDesktopCaptureSource, but limits selection  to tabs. This solves the issue of kAutoSelectDesktopCaptureSource being  liable to accidentally capturing the Chromium window instead of the tab,  as both have the same title if the tab is focused. | kAutoSelectTabCaptureSourceByTitle |  | ../chromium/src/chrome/common/chrome_switches.cc |
| --auto-select-window-capture-source-by-title |  This flag makes Chrome auto-select a window with the provided title when  the media-picker should otherwise be displayed to the user. This switch  is very similar to kAutoSelectDesktopCaptureSource, but limits selection  to the window. | kAutoSelectWindowCaptureSourceByTitle |  | ../chromium/src/chrome/common/chrome_switches.cc |
| --bypass-account-already-used-by-another-profile-check |  If specified, allows syncing multiple profiles to the same account. Used for  multi-client E2E tests. | kBypassAccountAlreadyUsedByAnotherProfileCheck |  | ../chromium/src/chrome/common/chrome_switches.cc |
| --check-for-update-interval |  How often (in seconds) to check for updates. Should only be used for testing  purposes. | kCheckForUpdateIntervalSec |  | ../chromium/src/chrome/common/chrome_switches.cc |
| --cipher-suite-blacklist |  Comma-separated list of SSL cipher suites to disable. | kCipherSuiteBlacklist |  | ../chromium/src/chrome/common/chrome_switches.cc |
| --crash-on-hang-threads |  Comma-separated list of BrowserThreads that cause browser process to crash if  the given browser thread is not responsive. UI/IO are the BrowserThreads that  are supported.   For example:     --crash-on-hang-threads=UI:18,IO:18 --> Crash the browser if UI or IO is     not responsive for 18 seconds while the other browser thread is     responsive. | kCrashOnHangThreads |  | ../chromium/src/chrome/common/chrome_switches.cc |
| --create-browser-on-startup-for-tests |  Some platforms like ChromeOS default to empty desktop.  Browser tests may need to add this switch so that at least one browser  instance is created on startup.  TODO(nkostylev): Investigate if this switch could be removed.  (http:crbug.com/148675) | kCreateBrowserOnStartupForTests |  | ../chromium/src/chrome/common/chrome_switches.cc |
| --credits |  Prints licensing information (same content as found in about:credits) and  quits. | kCredits |  | ../chromium/src/chrome/common/chrome_switches.cc |
| --custom-devtools-frontend |  Specifies the http: endpoint which will be used to serve  devtools:devtools/custom/<path>  Or a file: URL to specify a custom file path to load from for  devtools:devtools/bundled/<path> | kCustomDevtoolsFrontend |  | ../chromium/src/chrome/common/chrome_switches.cc |
| --debug-packed-apps |  Adds debugging entries such as Inspect Element to context menus of packed  apps. | kDebugPackedApps |  | ../chromium/src/chrome/common/chrome_switches.cc |
| --devtools-flags |  Passes command line parameters to the DevTools front-end. | kDevToolsFlags |  | ../chromium/src/chrome/common/chrome_switches.cc |
| --diagnostics |  Triggers a plethora of diagnostic modes. | kDiagnostics |  | ../chromium/src/chrome/common/chrome_switches.cc |
| --diagnostics-format |  Sets the output format for diagnostic modes enabled by diagnostics flag. | kDiagnosticsFormat |  | ../chromium/src/chrome/common/chrome_switches.cc |
| --diagnostics-recovery |  Tells the diagnostics mode to do the requested recovery step(s). | kDiagnosticsRecovery |  | ../chromium/src/chrome/common/chrome_switches.cc |
| --disable-auto-maximize-for-tests |  Disables the auto maximize feature on ChromeOS so that a browser window  always starts in normal state. This is used by tests that do not want this  auto maximizing behavior. | kDisableAutoMaximizeForTests | BUILDFLAG(IS_CHROMEOS) | ../chromium/src/chrome/common/chrome_switches.cc |
| --disable-background-networking |  Disable several subsystems which run network requests in the background.  This is for use when doing network performance testing to avoid noise in the  measurements. | kDisableBackgroundNetworking |  | ../chromium/src/chrome/common/chrome_switches.cc |
| --disable-component-extensions-with-background-pages |  Disable default component extensions with background pages - useful for  performance tests where these pages may interfere with perf results. | kDisableComponentExtensionsWithBackgroundPages |  | ../chromium/src/chrome/common/chrome_switches.cc |
| --disable-component-update |  | kDisableComponentUpdate |  | ../chromium/src/chrome/common/chrome_switches.cc |
| --disable-crashpad-for-testing |  Disables crashpad initialization for testing. The crashpad binary will not  run, and thus will not detect and symbolize crashes. | kDisableCrashpadForTesting |  | ../chromium/src/chrome/common/chrome_switches.cc |
| --disable-default-apps |  Disables installation of default apps on first run. This is used during  automated testing. | kDisableDefaultApps |  | ../chromium/src/chrome/common/chrome_switches.cc |
| --disable-domain-reliability |  Disables Domain Reliability Monitoring. | kDisableDomainReliability |  | ../chromium/src/chrome/common/chrome_switches.cc |
| --disable-extensions |  Disable extensions. | kDisableExtensions |  | ../chromium/src/chrome/common/chrome_switches.cc |
| --disable-extensions-except |  Disable extensions except those specified in a comma-separated list. | kDisableExtensionsExcept |  | ../chromium/src/chrome/common/chrome_switches.cc |
| --disable-lazy-loading |  Disables lazy loading of images and frames. | kDisableLazyLoading |  | ../chromium/src/chrome/common/chrome_switches.cc |
| --disable-nacl |  Disables NaCl. If kEnableNaCl is also set, this switch takes precedence. | kDisableNaCl |  | ../chromium/src/chrome/common/chrome_switches.cc |
| --disable-print-preview |  Disables print preview (For testing, and for users who don't like us. :[ ) | kDisablePrintPreview |  | ../chromium/src/chrome/common/chrome_switches.cc |
| --disable-prompt-on-repost |  Normally when the user attempts to navigate to a page that was the result of  a post we prompt to make sure they want to. This switch may be used to  disable that check. This switch is used during automated testing. | kDisablePromptOnRepost |  | ../chromium/src/chrome/common/chrome_switches.cc |
| --disable-stack-profiler |  Disable stack profiling. Stack profiling may change performance. Disabling  stack profiling is beneficial when comparing performance metrics with a  build that has it disabled by default. | kDisableStackProfiler |  | ../chromium/src/chrome/common/chrome_switches.cc |
| --disable-zero-browsers-open-for-tests |  Some tests seem to require the application to close when the last  browser window is closed. Thus, we need a switch to force this behavior  for ChromeOS Aura, disable "zero window mode".  TODO(pkotwicz): Investigate if this bug can be removed.  (http:crbug.com/119175) | kDisableZeroBrowsersOpenForTests |  | ../chromium/src/chrome/common/chrome_switches.cc |
| --disk-cache-dir |  Use a specific disk cache location, rather than one derived from the  UserDatadir. | kDiskCacheDir |  | ../chromium/src/chrome/common/chrome_switches.cc |
| --disk-cache-size |  Forces the maximum disk space to be used by the disk cache, in bytes. | kDiskCacheSize |  | ../chromium/src/chrome/common/chrome_switches.cc |
| --dump-browser-histograms |  Requests that a running browser process dump its collected histograms to a  given file. The file is overwritten if it exists. | kDumpBrowserHistograms |  | ../chromium/src/chrome/common/chrome_switches.cc |
| --enable-audio-debug-recordings-from-extension |  If the WebRTC logging private API is active, enables audio debug recordings. | kEnableAudioDebugRecordingsFromExtension |  | ../chromium/src/chrome/common/chrome_switches.cc |
| --enable-bookmark-undo |  Enables the multi-level undo system for bookmarks. | kEnableBookmarkUndo |  | ../chromium/src/chrome/common/chrome_switches.cc |
| --enable-cloud-print-proxy |  This applies only when the process type is "service". Enables the Cloud Print  Proxy component within the service process. | kEnableCloudPrintProxy |  | ../chromium/src/chrome/common/chrome_switches.cc |
| --enable-domain-reliability |  Enables Domain Reliability Monitoring. | kEnableDomainReliability |  | ../chromium/src/chrome/common/chrome_switches.cc |
| --enable-download-warning-improvements |  Enables a number of UI improvements to downloads, download scanning, and  download warnings. | kEnableDownloadWarningImprovements |  | ../chromium/src/chrome/common/chrome_switches.cc |
| --enable-extension-activity-logging |  Enables logging for extension activity. | kEnableExtensionActivityLogging |  | ../chromium/src/chrome/common/chrome_switches.cc |
| --enable-extension-activity-log-testing |  | kEnableExtensionActivityLogTesting |  | ../chromium/src/chrome/common/chrome_switches.cc |
| --enable-unsafe-extension-debugging |  Enables installing/uninstalling extensions at runtime via Chrome DevTools  Protocol if the protocol client is connected over --remote-debugging-pipe. | kEnableUnsafeExtensionDebugging |  | ../chromium/src/chrome/common/chrome_switches.cc |
| --enable-hangout-services-extension-for-testing |  Force enabling HangoutServicesExtension. | kEnableHangoutServicesExtensionForTesting |  | ../chromium/src/chrome/common/chrome_switches.cc |
| --enable-nacl |  Allows NaCl to run in all contexts (such as open web). Note that  kDisableNaCl disables NaCl in all contexts and takes precedence. | kEnableNaCl |  | ../chromium/src/chrome/common/chrome_switches.cc |
| --enable-net-benchmarking |  Enables the network-related benchmarking extensions. | kEnableNetBenchmarking |  | ../chromium/src/chrome/common/chrome_switches.cc |
| --enable-potentially-annoying-security-features |  Enables a number of potentially annoying security features (strict mixed  content mode, powerful feature restrictions, etc.) | kEnablePotentiallyAnnoyingSecurityFeatures |  | ../chromium/src/chrome/common/chrome_switches.cc |
| --explicitly-allowed-ports |  Allows overriding the list of restricted ports by passing a comma-separated  list of port numbers. | kExplicitlyAllowedPorts |  | ../chromium/src/chrome/common/chrome_switches.cc |
| --extension-ai-data-collection |  Name of the command line flag to allow the ai data collection extension API. | kExtensionAiDataCollection |  | ../chromium/src/chrome/common/chrome_switches.cc |
| --extension-content-verification |  Name of the command line flag to force content verification to be on in one  of various modes. | kExtensionContentVerification |  | ../chromium/src/chrome/common/chrome_switches.cc |
| --bootstrap |  Values for the kExtensionContentVerification flag.  See ContentVerifierDelegate::Mode for more explanation. | kExtensionContentVerificationBootstrap |  | ../chromium/src/chrome/common/chrome_switches.cc |
| --enforce |  | kExtensionContentVerificationEnforce |  | ../chromium/src/chrome/common/chrome_switches.cc |
| --enforce_strict |  | kExtensionContentVerificationEnforceStrict |  | ../chromium/src/chrome/common/chrome_switches.cc |
| --extensions-install-verification |  Turns on extension install verification if it would not otherwise have been  turned on. | kExtensionsInstallVerification |  | ../chromium/src/chrome/common/chrome_switches.cc |
| --extensions-not-webstore |  Specifies a comma-separated list of extension ids that should be forced to  be treated as not from the webstore when doing install verification. | kExtensionsNotWebstore |  | ../chromium/src/chrome/common/chrome_switches.cc |
| --extensions-toolbar-zero-state-variation |  Specifies the variation of Zero State extensions toolbar recommendation to  show.  When a user with zero extensions installed clicks on the extensions puzzle  piece in the Chrome toolbar, Chrome displays a submenu suggesting the user  to explore the Chrome Web Store. | kExtensionsToolbarZeroStateVariation |  | ../chromium/src/chrome/common/chrome_switches.cc |
| --extensions-toolbar-zero-state-single-web-store-link |  This variation of the Zero State extensions toolbar recommendation presents  the user with a single link to the Chrome Web Store home page. | kExtensionsToolbarZeroStateSingleWebStoreLink |  | ../chromium/src/chrome/common/chrome_switches.cc |
| --extensions-toolbar-zero-state-explore-extensions-by-category |  This variation of the Zero State extensions toolbar recommendation suggests  extension categories the user can explore in the Chrome Web Store.  (e.g. find coupons, increase productivity) | kExtensionsToolbarZeroStateExploreExtensionsByCategory |  | ../chromium/src/chrome/common/chrome_switches.cc |
| --force-app-mode |  Forces application mode. This hides certain system UI elements and forces  the app to be installed if it hasn't been already. | kForceAppMode |  | ../chromium/src/chrome/common/chrome_switches.cc |
| --force-devtools-available |  Forces developer tools availability, no matter what values the enterprise  policies DeveloperToolsDisabled and DeveloperToolsAvailability are set to. | kForceDevToolsAvailable | BUILDFLAG(IS_CHROMEOS) | ../chromium/src/chrome/common/chrome_switches.cc |
| --force-first-run |  Displays the First Run experience when the browser is started, regardless of  whether or not it's actually the First Run (this overrides kNoFirstRun). | kForceFirstRun |  | ../chromium/src/chrome/common/chrome_switches.cc |
| --force-whats-new |  Displays the What's New experience when the browser is started if it has not  yet been shown for the current milestone (this overrides kNoFirstRun, without  showing the First Run experience). | kForceWhatsNew |  | ../chromium/src/chrome/common/chrome_switches.cc |
| --hide-crash-restore-bubble |  Does not show the crash restore bubble when the browser is started during the  system startup phase in ChromeOS, if the ChromeOS full restore feature is  enabled, because the ChromeOS full restore notification is shown for the user  to select restore or not. | kHideCrashRestoreBubble |  | ../chromium/src/chrome/common/chrome_switches.cc |
| --homepage |  Specifies which page will be displayed in newly-opened tabs. We need this  for testing purposes so that the UI tests don't depend on what comes up for  http:google.com. | kHomePage |  | ../chromium/src/chrome/common/chrome_switches.cc |
| --incognito |  Causes the initial browser opened to be in incognito mode. Further browsers  may or may not be in incognito mode; see `IncognitoModePrefs`. | kIncognito |  | ../chromium/src/chrome/common/chrome_switches.cc |
| --initial-preferences-file |  Manually sets the initial preferences file. This is required to change the  initial preferences when the default file is read-only (eg. on lacros).  Passing this flag will reset the preferences regardless of whether this is  the first run. | kInitialPreferencesFile | BUILDFLAG(IS_CHROMEOS_LACROS) | ../chromium/src/chrome/common/chrome_switches.cc |
| --init-isolate-as-foreground |  Specifies that the main-thread Isolate should initialize in foreground mode.  If not specified, the the Isolate will start in background mode for extension  processes and foreground mode otherwise. | kInitIsolateAsForeground |  | ../chromium/src/chrome/common/chrome_switches.cc |
| --install-autogenerated-theme |  Installs an autogenerated theme based on the given RGB value.  The format is "r,g,b", where r, g, b are a numeric values from 0 to 255. | kInstallAutogeneratedTheme |  | ../chromium/src/chrome/common/chrome_switches.cc |
| --install-chrome-app |  Causes Chrome to initiate an installation flow for the given app. | kInstallChromeApp |  | ../chromium/src/chrome/common/chrome_switches.cc |
| --install-isolated-web-app-from-file |  Causes Chrome to install the unsigned Web Bundle at the given path as a  developer mode Isolated Web App. | kInstallIsolatedWebAppFromFile |  | ../chromium/src/chrome/common/chrome_switches.cc |
| --install-isolated-web-app-from-url |  Causes Chrome to install a developer mode Isolated Web App whose contents  are hosted at the given HTTP(S) URL. | kInstallIsolatedWebAppFromUrl |  | ../chromium/src/chrome/common/chrome_switches.cc |
| --instant-process |  Marks a renderer as an Instant process. | kInstantProcess |  | ../chromium/src/chrome/common/chrome_switches.cc |
| --keep-alive-for-test |  Used for testing - keeps browser alive after last browser window closes. | kKeepAliveForTest |  | ../chromium/src/chrome/common/chrome_switches.cc |
| --kiosk |  Enable kiosk mode. Please note this is not Chrome OS kiosk mode. | kKioskMode |  | ../chromium/src/chrome/common/chrome_switches.cc |
| --kiosk-printing |  Enable automatically pressing the print button in print preview. | kKioskModePrinting |  | ../chromium/src/chrome/common/chrome_switches.cc |
| --make-default-browser |  Makes Chrome default browser | kMakeDefaultBrowser |  | ../chromium/src/chrome/common/chrome_switches.cc |
| --monitoring-destination-id |  Allows setting a different destination ID for connection-monitoring GCM  messages. Useful when running against a non-prod management server. | kMonitoringDestinationID |  | ../chromium/src/chrome/common/chrome_switches.cc |
| --native-messaging-connect-host |  Requests a native messaging connection be established between the native  messaging host named by this switch and the extension with ID specified by  kNativeMessagingConnectExtension. | kNativeMessagingConnectHost |  | ../chromium/src/chrome/common/chrome_switches.cc |
| --native-messaging-connect-extension |  Requests a native messaging connection be established between the extension  with ID specified by this switch and the native messaging host named by the  kNativeMessagingConnectHost switch. | kNativeMessagingConnectExtension |  | ../chromium/src/chrome/common/chrome_switches.cc |
| --native-messaging-connect-id |  If set when kNativeMessagingConnectHost and kNativeMessagingConnectExtension  are specified, is reflected to the native messaging host as a command line  parameter. | kNativeMessagingConnectId |  | ../chromium/src/chrome/common/chrome_switches.cc |
| --no-default-browser-check |  Disables the default browser check. Useful for UI/browser tests where we  want to avoid having the default browser info-bar displayed. | kNoDefaultBrowserCheck |  | ../chromium/src/chrome/common/chrome_switches.cc |
| --no-experiments |  Disables all experiments set on about:flags. Does not disable about:flags  itself. Useful if an experiment makes chrome crash at startup: One can start  chrome with --no-experiments, disable the problematic lab at about:flags and  then restart chrome without this switch again. | kNoExperiments |  | ../chromium/src/chrome/common/chrome_switches.cc |
| --no-first-run |  Skip First Run tasks as well as not showing additional dialogs, prompts or  bubbles. Suppressing dialogs, prompts, and bubbles is important as this  switch is used by automation (including performance benchmarks) where it's  important only a browser window is shown.   This may not actually be the first run or the What's New page. Its effect can  be partially ignored by adding kForceFirstRun (for FRE), kForceWhatsNew (for  What's New) and/or kIgnoreNoFirstRunForSearchEngineChoiceScreen (for the DSE  choice screen). This does not drop the First Run sentinel and thus doesn't  prevent first run from occurring the next time chrome is launched without  this flag. It also does not update the last What's New milestone, so does not  prevent What's New from occurring the next time chrome is launched without  this flag. | kNoFirstRun |  | ../chromium/src/chrome/common/chrome_switches.cc |
| --no-pings |  Don't send hyperlink auditing pings | kNoPings |  | ../chromium/src/chrome/common/chrome_switches.cc |
| --no-proxy-server |  Don't use a proxy server, always make direct connections. Overrides any  other proxy server flags that are passed. | kNoProxyServer |  | ../chromium/src/chrome/common/chrome_switches.cc |
| --no-service-autorun |  Disables the service process from adding itself as an autorun process. This  does not delete existing autorun registrations, it just prevents the service  from registering a new one. | kNoServiceAutorun |  | ../chromium/src/chrome/common/chrome_switches.cc |
| --no-startup-window |  Does not automatically open a browser window on startup (used when  launching Chrome for the purpose of hosting background apps). | kNoStartupWindow |  | ../chromium/src/chrome/common/chrome_switches.cc |
| --on-the-fly-mhtml-hash-computation |  Calculate the hash of an MHTML file as it is being saved.  The browser process will write the serialized MHTML contents to a file and  calculate its hash as it is streamed back from the renderer via a Mojo data  pipe. | kOnTheFlyMhtmlHashComputation |  | ../chromium/src/chrome/common/chrome_switches.cc |
| --new-window |  Launches URL in new browser window. | kOpenInNewWindow |  | ../chromium/src/chrome/common/chrome_switches.cc |
| --pack-extension |  Packages an extension to a .crx installable file from a given directory. | kPackExtension |  | ../chromium/src/chrome/common/chrome_switches.cc |
| --pack-extension-key |  Optional PEM private key to use in signing packaged .crx. | kPackExtensionKey |  | ../chromium/src/chrome/common/chrome_switches.cc |
| --pre-crashpad-crash-test |  Causes the browser process to crash very early in startup, just before  crashpad (or breakpad) is initialized. | kPreCrashpadCrashTest |  | ../chromium/src/chrome/common/chrome_switches.cc |
| --prediction-service-mock-likelihood |  Used to mock the response received from the Web Permission Prediction  Service. Used for testing. | kPredictionServiceMockLikelihood |  | ../chromium/src/chrome/common/chrome_switches.cc |
| --preinstalled-web-apps-dir |  A directory where Chrome looks for json files describing default/preinstalled  web apps. This overrides any default directory to load preinstalled web apps  from. | kPreinstalledWebAppsDir |  | ../chromium/src/chrome/common/chrome_switches.cc |
| --privet-ipv6-only |  Use IPv6 only for privet HTTP. | kPrivetIPv6Only |  | ../chromium/src/chrome/common/chrome_switches.cc |
| --product-version |  Outputs the product version information and quit. Used as an internal api to  detect the installed version of Chrome on Linux. | kProductVersion |  | ../chromium/src/chrome/common/chrome_switches.cc |
| --profile-directory |  Selects directory of profile to associate with the first browser launched. | kProfileDirectory |  | ../chromium/src/chrome/common/chrome_switches.cc |
| --ignore-profile-directory-if-not-exists |  If provided with kProfileDirectory, does not create the profile if the  profile directory doesn't exist. | kIgnoreProfileDirectoryIfNotExists |  | ../chromium/src/chrome/common/chrome_switches.cc |
| --profile-email |  Like kProfileDirectory, but selects the profile by email address. If the  email is not found in any existing profile, this switch has no effect. If  both kProfileDirectory and kProfileUserName are specified, kProfileDirectory  takes priority. | kProfileEmail |  | ../chromium/src/chrome/common/chrome_switches.cc |
| --proxy-auto-detect |  Forces proxy auto-detection. | kProxyAutoDetect |  | ../chromium/src/chrome/common/chrome_switches.cc |
| --proxy-bypass-list |  Specifies a list of hosts for whom we bypass proxy settings and use direct  connections. Ignored if --proxy-auto-detect or --no-proxy-server are also  specified. This is a comma-separated list of bypass rules. See:  "net/proxy_resolution/proxy_bypass_rules.h" for the format of these rules. | kProxyBypassList |  | ../chromium/src/chrome/common/chrome_switches.cc |
| --proxy-pac-url |  Uses the pac script at the given URL | kProxyPacUrl |  | ../chromium/src/chrome/common/chrome_switches.cc |
| --proxy-server |  Uses a specified proxy server, overrides system settings. | kProxyServer |  | ../chromium/src/chrome/common/chrome_switches.cc |
| --remote-debugging-targets |  Provides a list of addresses to discover DevTools remote debugging targets.  The format is <host>:<port>,...,<host>:port. | kRemoteDebuggingTargets |  | ../chromium/src/chrome/common/chrome_switches.cc |
| --restart |  Indicates that Chrome was restarted (e.g., after a flag change). This is used  to ignore the launch when recording the Launch.Mode2 metric. | kRestart |  | ../chromium/src/chrome/common/chrome_switches.cc |
| --restore-last-session |  Indicates the last session should be restored on startup. This overrides the  preferences value. Note that this does not force automatic session restore  following a crash, so as to prevent a crash loop. This switch is used to  implement support for OS-specific "continue where you left off" functionality  on OS X and Windows. | kRestoreLastSession |  | ../chromium/src/chrome/common/chrome_switches.cc |
| --save-page-as-mhtml |  Disable saving pages as HTML-only, disable saving pages as HTML Complete  (with a directory of sub-resources). Enable only saving pages as MHTML.  See http:crbug.com/120416 for how to remove this switch. | kSavePageAsMHTML |  | ../chromium/src/chrome/common/chrome_switches.cc |
| --screen-capture-audio-default-unchecked |  This flag sets the checkboxes for sharing audio during screen capture to off  by default. It is primarily intended to be used for tests. | kScreenCaptureAudioDefaultUnchecked |  | ../chromium/src/chrome/common/chrome_switches.cc |
| --silent-debugger-extension-api |  Does not show an infobar when an extension attaches to a page using  chrome.debugger page. Required to attach to extension background pages. | kSilentDebuggerExtensionAPI |  | ../chromium/src/chrome/common/chrome_switches.cc |
| --silent-launch |  Causes Chrome to launch without opening any windows by default. Useful if  one wishes to use Chrome as an ash server. | kSilentLaunch |  | ../chromium/src/chrome/common/chrome_switches.cc |
| --simulate-browsing-data-lifetime |  Sets the BrowsingDataLifetime policy to a very short value (shorter than  normally possible) for testing purposes. | kSimulateBrowsingDataLifetime |  | ../chromium/src/chrome/common/chrome_switches.cc |
| --simulate-critical-update |  Simulates a critical update being available. | kSimulateCriticalUpdate |  | ../chromium/src/chrome/common/chrome_switches.cc |
| --simulate-elevated-recovery |  Simulates that elevation is needed to recover upgrade channel. | kSimulateElevatedRecovery |  | ../chromium/src/chrome/common/chrome_switches.cc |
| --simulate-outdated |  Simulates that current version is outdated. | kSimulateOutdated |  | ../chromium/src/chrome/common/chrome_switches.cc |
| --simulate-outdated-no-au |  Simulates that current version is outdated and auto-update is off. | kSimulateOutdatedNoAU |  | ../chromium/src/chrome/common/chrome_switches.cc |
| --simulate-upgrade |  Simulates an update being available. | kSimulateUpgrade |  | ../chromium/src/chrome/common/chrome_switches.cc |
| --simulate-idle-timeout |  Sets the IdleTimeout policy to a very short value (shorter than normally  possible) for testing purposes. | kSimulateIdleTimeout |  | ../chromium/src/chrome/common/chrome_switches.cc |
| --ssl-version-max |  Specifies the maximum SSL/TLS version ("tls1.2" or "tls1.3"). | kSSLVersionMax |  | ../chromium/src/chrome/common/chrome_switches.cc |
| --ssl-version-min |  Specifies the minimum SSL/TLS version ("tls1.2" or "tls1.3"). | kSSLVersionMin |  | ../chromium/src/chrome/common/chrome_switches.cc |
| --tls1.2 |  TLS 1.2 mode for |kSSLVersionMax| and |kSSLVersionMin| switches. | kSSLVersionTLSv12 |  | ../chromium/src/chrome/common/chrome_switches.cc |
| --tls1.3 |  TLS 1.3 mode for |kSSLVersionMax| and |kSSLVersionMin| switches. | kSSLVersionTLSv13 |  | ../chromium/src/chrome/common/chrome_switches.cc |
| --start-maximized |  Starts the browser maximized, regardless of any previous settings. | kStartMaximized |  | ../chromium/src/chrome/common/chrome_switches.cc |
| --start-stack-profiler |  Starts the stack sampling profiler in the child process. | kStartStackProfiler |  | ../chromium/src/chrome/common/chrome_switches.cc |
| --browser-test |  Browser test mode for the |kStartStackProfiler| switch. Limits the profile  durations to be significantly less than the test timeout. On ChromeOS,  forces the stack sampling profiler to run on all processes as well. | kStartStackProfilerBrowserTest |  | ../chromium/src/chrome/common/chrome_switches.cc |
| --storage-pressure-notification-interval |  Interval, in minutes, used for storage pressure notification throttling.  Useful for developers testing applications that might use non-trivial  amounts of disk space. | kStoragePressureNotificationInterval |  | ../chromium/src/chrome/common/chrome_switches.cc |
| --system-log-upload-frequency |  Frequency in Milliseconds for system log uploads. Should only be used for  testing purposes. | kSystemLogUploadFrequency |  | ../chromium/src/chrome/common/chrome_switches.cc |
| --auto-accept-this-tab-capture |  This flag makes Chrome auto-accept/reject requests to capture the current  tab. It should only be used for tests. | kThisTabCaptureAutoAccept |  | ../chromium/src/chrome/common/chrome_switches.cc |
| --auto-reject-this-tab-capture |  | kThisTabCaptureAutoReject |  | ../chromium/src/chrome/common/chrome_switches.cc |
| --test-memory-log-delay-in-minutes |  Custom delay for memory log. This should be used only for testing purpose. | kTestMemoryLogDelayInMinutes |  | ../chromium/src/chrome/common/chrome_switches.cc |
| --test-name |  Passes the name of the current running automated test to Chrome. | kTestName |  | ../chromium/src/chrome/common/chrome_switches.cc |
| --trusted-download-sources |  Identifies a list of download sources as trusted, but only if proper group  policy is set. | kTrustedDownloadSources |  | ../chromium/src/chrome/common/chrome_switches.cc |
| --unlimited-storage |  Overrides per-origin quota settings to unlimited storage for any  apps/origins.  This should be used only for testing purpose. | kUnlimitedStorage |  | ../chromium/src/chrome/common/chrome_switches.cc |
| --unsafely-disable-devtools-self-xss-warnings |  Disables warnings about self-XSS attacks when pasting into the DevTools  console. | kUnsafelyDisableDevToolsSelfXssWarnings |  | ../chromium/src/chrome/common/chrome_switches.cc |
| --user-data-dir |  Specifies the user data directory, which is where the browser will look for  all of its state. | kUserDataDir |  | ../chromium/src/chrome/common/chrome_switches.cc |
| --use-system-proxy-resolver |  Uses WinHttp to resolve proxies instead of using Chromium's normal proxy  resolution logic. This is only supported in Windows.   TODO(crbug.com/40111093): Only use WinHttp whenever Chrome is  exclusively using system proxy configs. | kUseSystemProxyResolver |  | ../chromium/src/chrome/common/chrome_switches.cc |
| --validate-crx |  Examines a .crx for validity and prints the result. | kValidateCrx |  | ../chromium/src/chrome/common/chrome_switches.cc |
| --version |  Prints version information and quits. | kVersion |  | ../chromium/src/chrome/common/chrome_switches.cc |
| --webrtc-event-log-proactive-pruning-delta |  Sets the delay (in seconds) between proactive prunings of remote-bound  WebRTC event logs which are pending upload.  All positive values are legal.  All negative values are illegal, and ignored.  If set to 0, the meaning is "no proactive pruning". | kWebRtcRemoteEventLogProactivePruningDelta |  | ../chromium/src/chrome/common/chrome_switches.cc |
| --webrtc-event-log-upload-delay-ms |  WebRTC event logs will only be uploaded if the conditions hold for this  many milliseconds. | kWebRtcRemoteEventLogUploadDelayMs |  | ../chromium/src/chrome/common/chrome_switches.cc |
| --webrtc-event-log-upload-no-suppression |  Normally, remote-bound WebRTC event logs are uploaded only when no  peer connections are active. With this flag, the upload is never suppressed. | kWebRtcRemoteEventLogUploadNoSuppression |  | ../chromium/src/chrome/common/chrome_switches.cc |
| --webrtc-ip-handling-policy |  Override WebRTC IP handling policy to mimic the behavior when WebRTC IP  handling policy is specified in Preferences. | kWebRtcIPHandlingPolicy |  | ../chromium/src/chrome/common/chrome_switches.cc |
| --window-name |  Specify the initial window user title: --window-name="My custom title" | kWindowName |  | ../chromium/src/chrome/common/chrome_switches.cc |
| --window-position |  Specify the initial window position: --window-position=x,y | kWindowPosition |  | ../chromium/src/chrome/common/chrome_switches.cc |
| --window-size |  Specify the initial window size: --window-size=w,h | kWindowSize |  | ../chromium/src/chrome/common/chrome_switches.cc |
| --window-workspace |  Specify the initial window workspace: --window-workspace=id | kWindowWorkspace |  | ../chromium/src/chrome/common/chrome_switches.cc |
| --winhttp-proxy-resolver |  Uses WinHTTP to fetch and evaluate PAC scripts. Otherwise the default is to  use Chromium's network stack to fetch, and V8 to evaluate. | kWinHttpProxyResolver |  | ../chromium/src/chrome/common/chrome_switches.cc |
| --win-jumplist-action |  Specifies which category option was clicked in the Windows Jumplist that  resulted in a browser startup. | kWinJumplistAction |  | ../chromium/src/chrome/common/chrome_switches.cc |
| --auth-spnego-account-type |  Android authentication account type for SPNEGO authentication | kAuthAndroidNegotiateAccountType | BUILDFLAG(IS_ANDROID) | ../chromium/src/chrome/common/chrome_switches.cc |
| --force-device-ownership |  Forces the device to report being owned by an enterprise. This mimics the  presence of an app signaling device ownership. | kForceDeviceOwnership | BUILDFLAG(IS_ANDROID) | ../chromium/src/chrome/common/chrome_switches.cc |
| --force-enable-night-mode |  Forces the night mode to be enabled. | kForceEnableNightMode | BUILDFLAG(IS_ANDROID) | ../chromium/src/chrome/common/chrome_switches.cc |
| --force-show-update-menu-badge |  Forces the update menu badge to show. | kForceShowUpdateMenuBadge | BUILDFLAG(IS_ANDROID) | ../chromium/src/chrome/common/chrome_switches.cc |
| --force-update-menu-type |  Forces the update menu type to a specific type. | kForceUpdateMenuType | BUILDFLAG(IS_ANDROID) | ../chromium/src/chrome/common/chrome_switches.cc |
| --custom_summary |  Forces a custom summary to be displayed below the update menu item. | kForceShowUpdateMenuItemCustomSummary | BUILDFLAG(IS_ANDROID) | ../chromium/src/chrome/common/chrome_switches.cc |
| --market-url-for-testing |  Sets the market URL for Chrome for use in testing. | kMarketUrlForTesting | BUILDFLAG(IS_ANDROID) | ../chromium/src/chrome/common/chrome_switches.cc |
| --request-desktop-sites |  Force enable user agent overrides to request desktop sites in Clank. | kRequestDesktopSites | BUILDFLAG(IS_ANDROID) | ../chromium/src/chrome/common/chrome_switches.cc |
| --crosh-command |  Custom crosh command. | kCroshCommand | BUILDFLAG(IS_CHROMEOS_ASH) | ../chromium/src/chrome/common/chrome_switches.cc |
| --disable-logging-redirect |  Disables logging redirect for testing. | kDisableLoggingRedirect | BUILDFLAG(IS_CHROMEOS_ASH) | ../chromium/src/chrome/common/chrome_switches.cc |
| --disable-login-screen-apps |  Disables apps on the login screen. By default, they are allowed and can be  installed through policy. | kDisableLoginScreenApps | BUILDFLAG(IS_CHROMEOS_ASH) | ../chromium/src/chrome/common/chrome_switches.cc |
| --short-merge-session-timeout-for-test |  Use a short (1 second) timeout for merge session loader throttle testing. | kShortMergeSessionTimeoutForTest | BUILDFLAG(IS_CHROMEOS_ASH) | ../chromium/src/chrome/common/chrome_switches.cc |
| --scheduler-configuration |  Selects the scheduler configuration specified in the parameter. | kSchedulerConfiguration | BUILDFLAG(IS_CHROMEOS_ASH) | ../chromium/src/chrome/common/chrome_switches.cc |
| --conservative |  | kSchedulerConfigurationConservative | BUILDFLAG(IS_CHROMEOS_ASH) | ../chromium/src/chrome/common/chrome_switches.cc |
| --performance |  | kSchedulerConfigurationPerformance | BUILDFLAG(IS_CHROMEOS_ASH) | ../chromium/src/chrome/common/chrome_switches.cc |
| --scheduler-configuration-default |  Specifies what the default scheduler configuration value is if the user does  not set one. | kSchedulerConfigurationDefault | BUILDFLAG(IS_CHROMEOS_ASH) | ../chromium/src/chrome/common/chrome_switches.cc |
| --help |  These flags show the man page on Linux. They are equivalent to each  other. | kHelp | BUILDFLAG(IS_POSIX) && !BUILDFLAG(IS_MAC) && !BUILDFLAG(IS_CHROMEOS_ASH) | ../chromium/src/chrome/common/chrome_switches.cc |
| --h |  | kHelpShort | BUILDFLAG(IS_POSIX) && !BUILDFLAG(IS_MAC) && !BUILDFLAG(IS_CHROMEOS_ASH) | ../chromium/src/chrome/common/chrome_switches.cc |
| --class |  The same as the --class argument in X applications.  Overrides the WM_CLASS  window property with the given value. | kWmClass | BUILDFLAG(IS_POSIX) && !BUILDFLAG(IS_MAC) && !BUILDFLAG(IS_CHROMEOS_ASH) | ../chromium/src/chrome/common/chrome_switches.cc |
| --apps-keep-chrome-alive-in-tests |  Prevents Chrome from quitting when Chrome Apps are open. | kAppsKeepChromeAliveInTests | BUILDFLAG(IS_MAC) | ../chromium/src/chrome/common/chrome_switches.cc |
| --enable-user-metrics |  Enable user metrics from within the installer. | kEnableUserMetrics | BUILDFLAG(IS_MAC) | ../chromium/src/chrome/common/chrome_switches.cc |
| --metrics-client-id |  This is how the metrics client ID is passed from the browser process to its  children. With Crashpad, the metrics client ID is distinct from the crash  client ID. | kMetricsClientID | BUILDFLAG(IS_MAC) | ../chromium/src/chrome/common/chrome_switches.cc |
| --relauncher |  A process type (switches::kProcessType) that relaunches the browser. See  chrome/browser/mac/relauncher.h. | kRelauncherProcess | BUILDFLAG(IS_MAC) | ../chromium/src/chrome/common/chrome_switches.cc |
| --dmg-device |  When switches::kProcessType is switches::kRelauncherProcess, if this switch  is also present, the relauncher process will unmount and eject a mounted disk  image and move its disk image file to the trash.  The argument's value must  be a BSD device name of the form "diskN" or "diskNsM". | kRelauncherProcessDMGDevice | BUILDFLAG(IS_MAC) | ../chromium/src/chrome/common/chrome_switches.cc |
| --make-chrome-default |  Indicates whether Chrome should be set as the default browser during  installation. | kMakeChromeDefault | BUILDFLAG(IS_MAC) | ../chromium/src/chrome/common/chrome_switches.cc |
| --code-sign-clone-cleanup |  A process type (switches::kProcessType) that cleans up the browser's  temporary code sign clone. | kCodeSignCloneCleanupProcess | BUILDFLAG(IS_MAC) | ../chromium/src/chrome/common/chrome_switches.cc |
| --unique-temp-dir-suffix |  When switches::kProcessType is switches::kCodeSignCloneCleanupProcess this  switch is required. The value must be the unique suffix portion of the  temporary directory that contains the clone. The full path will be  reconstructed by the cleanup process. | kUniqueTempDirSuffix | BUILDFLAG(IS_MAC) | ../chromium/src/chrome/common/chrome_switches.cc |
| --enable-profile-shortcut-manager |  Force-enables the profile shortcut manager. This is needed for tests since  they use a custom-user-data-dir which disables this. | kEnableProfileShortcutManager | BUILDFLAG(IS_WIN) | ../chromium/src/chrome/common/chrome_switches.cc |
| --from-installer |  Indicates that this launch of the browser originated from the installer  (i.e., following a successful new install or over-install). This triggers  browser behaviors for this specific launch, such as a welcome announcement  for accessibility software (see https:crbug.com/1072735). | kFromInstaller | BUILDFLAG(IS_WIN) | ../chromium/src/chrome/common/chrome_switches.cc |
| --from-browser-switcher |  Indicates that this launch of the browser originated from the Legacy Browser  Support for Edge extension's native host. This is recorded in UMA. | kFromBrowserSwitcher | BUILDFLAG(IS_WIN) | ../chromium/src/chrome/common/chrome_switches.cc |
| --hide-icons |  Makes Windows happy by allowing it to show "Enable access to this program"  checkbox in Add/Remove Programs->Set Program Access and Defaults. This only  shows an error box because the only way to hide Chrome is by uninstalling  it. | kHideIcons | BUILDFLAG(IS_WIN) | ../chromium/src/chrome/common/chrome_switches.cc |
| --no-network-profile-warning |  Whether or not the browser should warn if the profile is on a network share.  This flag is only relevant for Windows currently. | kNoNetworkProfileWarning | BUILDFLAG(IS_WIN) | ../chromium/src/chrome/common/chrome_switches.cc |
| --no-pre-read-main-dll |  Whether this process should PrefetchVirtualMemory on the contents of  Chrome.dll. This warms up the pages in memory to speed up startup but might  not be required in later renderers and/or GPU. For experiment info see  crbug.com/1350257. | kNoPreReadMainDll | BUILDFLAG(IS_WIN) | ../chromium/src/chrome/common/chrome_switches.cc |
| --notification-inline-reply |  Used in combination with kNotificationLaunchId to specify the inline reply  entered in the toast in the Windows Action Center. | kNotificationInlineReply | BUILDFLAG(IS_WIN) | ../chromium/src/chrome/common/chrome_switches.cc |
| --notification-launch-id |  Used for launching Chrome when a toast displayed in the Windows Action Center  has been activated. Should contain the launch ID encoded by Chrome. | kNotificationLaunchId | BUILDFLAG(IS_WIN) | ../chromium/src/chrome/common/chrome_switches.cc |
| --show-icons |  See kHideIcons. | kShowIcons | BUILDFLAG(IS_WIN) | ../chromium/src/chrome/common/chrome_switches.cc |
| --source-shortcut |  When rendezvousing with an existing process, used to pass the path of the  shortcut that launched the new Chrome process. This is used to record launch  metrics. | kSourceShortcut | BUILDFLAG(IS_WIN) | ../chromium/src/chrome/common/chrome_switches.cc |
| --uninstall |  Runs un-installation steps that were done by chrome first-run. | kUninstall | BUILDFLAG(IS_WIN) | ../chromium/src/chrome/common/chrome_switches.cc |
| --uninstall-app-id |  Specifies that the WebApp with the specified id should be uninstalled. | kUninstallAppId | BUILDFLAG(IS_WIN) | ../chromium/src/chrome/common/chrome_switches.cc |
| --pwa-launcher-version |  Specifies the version of the Progressive-Web-App launcher that launched  Chrome, used to determine whether to update all launchers.  NOTE: changing this switch requires adding legacy handling for the previous  method, as older PWA launchers still using this switch will rely on Chrome to  update them to use the new method. | kPwaLauncherVersion | BUILDFLAG(IS_WIN) | ../chromium/src/chrome/common/chrome_switches.cc |
| --debug-print |  Enables support to debug printing subsystem. | kDebugPrint | BUILDFLAG(ENABLE_PRINT_PREVIEW) && !defined(OFFICIAL_BUILD) | ../chromium/src/chrome/common/chrome_switches.cc |
| --allow-nacl-crxfs-api |  Specifies comma-separated list of extension ids or hosts to grant  access to CRX file system APIs. | kAllowNaClCrxFsAPI | BUILDFLAG(ENABLE_PLUGINS) | ../chromium/src/chrome/common/chrome_switches.cc |
| --allow-nacl-file-handle-api |  Specifies comma-separated list of extension ids or hosts to grant  access to file handle APIs. | kAllowNaClFileHandleAPI | BUILDFLAG(ENABLE_PLUGINS) | ../chromium/src/chrome/common/chrome_switches.cc |
| --allow-nacl-socket-api |  Specifies comma-separated list of extension ids or hosts to grant  access to TCP/UDP socket APIs. | kAllowNaClSocketAPI | BUILDFLAG(ENABLE_PLUGINS) | ../chromium/src/chrome/common/chrome_switches.cc |
| --enable-new-app-menu-icon |  | kEnableNewAppMenuIcon | BUILDFLAG(IS_LINUX) || BUILDFLAG(IS_CHROMEOS) || BUILDFLAG(IS_MAC) ||     BUILDFLAG(IS_WIN) | ../chromium/src/chrome/common/chrome_switches.cc |
| --guest |  Causes the browser to launch directly in guest mode. | kGuest | BUILDFLAG(IS_LINUX) || BUILDFLAG(IS_CHROMEOS) || BUILDFLAG(IS_MAC) ||     BUILDFLAG(IS_WIN) | ../chromium/src/chrome/common/chrome_switches.cc |
| --list-apps |  Writes open and installed web apps for each profile to the specified file  without launching a new browser window or tab. Pass a absolute file path to  specify where to output the information. Can be used together with optional  --profile-base-name switch to only write information for a given profile. | kListApps | BUILDFLAG(IS_LINUX) || BUILDFLAG(IS_MAC) || BUILDFLAG(IS_WIN) | ../chromium/src/chrome/common/chrome_switches.cc |
| --profile-base-name |  Pass the basename of the profile directory to specify which profile to get  information. Only relevant when used with --list-apps switch. | kProfileBaseName | BUILDFLAG(IS_LINUX) || BUILDFLAG(IS_MAC) || BUILDFLAG(IS_WIN) | ../chromium/src/chrome/common/chrome_switches.cc |
| --profile-management-attributes |  Domains and associated SAML attributes for which third-party profile  management should be enabled. Input should be in JSON format. | kProfileManagementAttributes | BUILDFLAG(IS_LINUX) || BUILDFLAG(IS_MAC) || BUILDFLAG(IS_WIN) | ../chromium/src/chrome/common/chrome_switches.cc |
| --webapk-server-url |  Custom WebAPK server URL for the sake of testing. | kWebApkServerUrl | BUILDFLAG(IS_CHROMEOS_ASH) || BUILDFLAG(IS_ANDROID) | ../chromium/src/chrome/common/chrome_switches.cc |
| --use-system-default-printer |  Uses the system default printer as the initially selected destination in  print preview, instead of the most recently used destination. | kUseSystemDefaultPrinter | !BUILDFLAG(IS_CHROMEOS_ASH) && !BUILDFLAG(IS_ANDROID) | ../chromium/src/chrome/common/chrome_switches.cc |
| --user-data-migrated |  Indicates that this process is the product of a relaunch following migration  of User Data. | kUserDataMigrated | BUILDFLAG(ENABLE_DOWNGRADE_PROCESSING) | ../chromium/src/chrome/common/chrome_switches.cc |
| switch | description | variable | cpp condition | location |
| ------ | ----------- | -------- | ------------- | -------- |
| --also-emit-success-logs |  Also emit full event trace logs for successful tests. | kAlsoEmitSuccessLogs |  | ../chromium/src/chrome/test/base/test_switches.cc |
| --devtools-code-coverage |  Directory to output JavaScript code coverage. When supplied enables coverage  in selected browser tests. | kDevtoolsCodeCoverage |  | ../chromium/src/chrome/test/base/test_switches.cc |
| --perf-test-print-uma-means |  Show the mean value of histograms that native performance tests  are monitoring. Note that this is only applicable for PerformanceTest  subclasses. | kPerfTestPrintUmaMeans |  | ../chromium/src/chrome/test/base/test_switches.cc |
| switch | description | variable | cpp condition | location |
| ------ | ----------- | -------- | ------------- | -------- |
| --true |  Value indicating whether flag from command line switch is true. | kSwitchValueTrue |  | ../chromium/src/chromecast/base/chromecast_switches.cc |
| --false |  Value indicating whether flag from command line switch is false. | kSwitchValueFalse |  | ../chromium/src/chromecast/base/chromecast_switches.cc |
| --crash-server-url |  Server url to upload crash data to.  Default is "https:clients2.google.com/cr/report" for prod devices.  Default is "https:clients2.google.com/cr/staging_report" for non prod. | kCrashServerUrl |  | ../chromium/src/chromecast/base/chromecast_switches.cc |
| --daemon |  Switch to enable daemon-mode in crash_uploader. | kCrashUploaderDaemon |  | ../chromium/src/chromecast/base/chromecast_switches.cc |
| --disable-crash-reporter |  Switch to disable Crash reporting | kDisableCrashReporter |  | ../chromium/src/chromecast/base/chromecast_switches.cc |
| --disable-crashpad-forwarding |  Switch to disable Crashpad forwarding | kDisableCrashpadForwarding |  | ../chromium/src/chromecast/base/chromecast_switches.cc |
| --dumpstate-path |  Switch to dumpstate binary path. | kDumpstateBinPath |  | ../chromium/src/chromecast/base/chromecast_switches.cc |
| --enable-local-file-accesses |  Enable file accesses. It should not be enabled for most Cast devices. | kEnableLocalFileAccesses |  | ../chromium/src/chromecast/base/chromecast_switches.cc |
| --override-metrics-upload-url |  Override the URL to which metrics logs are sent for debugging. | kOverrideMetricsUploadUrl |  | ../chromium/src/chromecast/base/chromecast_switches.cc |
| --require-wlan |  Only connect to WLAN interfaces. | kRequireWlan |  | ../chromium/src/chromecast/base/chromecast_switches.cc |
| --last-launched-app |  Pass the app id information to the renderer process, to be used for logging.  last-launched-app should be the app that just launched and is spawning the  renderer. | kLastLaunchedApp |  | ../chromium/src/chromecast/base/chromecast_switches.cc |
| --previous-app |  previous-app should be the app that was running when last-launched-app  started. | kPreviousApp |  | ../chromium/src/chromecast/base/chromecast_switches.cc |
| --accept-resource-provider |  Flag indicating that a resource provider must be set up to provide cast  receiver with resources. Apps cannot start until provided resources.  This flag implies --alsa-check-close-timeout=0. | kAcceptResourceProvider |  | ../chromium/src/chromecast/base/chromecast_switches.cc |
| --alsa-amp-device-name |  Name of the device the amp mixer should be opened on. If this flag is not  specified it will default to the same device as kAlsaVolumeDeviceName. | kAlsaAmpDeviceName |  | ../chromium/src/chromecast/base/chromecast_switches.cc |
| --alsa-amp-element-name |  Name of the simple mixer control element that the ALSA-based media library  should use to toggle powersave mode on the system. | kAlsaAmpElementName |  | ../chromium/src/chromecast/base/chromecast_switches.cc |
| --alsa-check-close-timeout |  Time in ms to wait before closing the PCM handle when no more mixer inputs  remain. Assumed to be 0 if --accept-resource-provider is present. | kAlsaCheckCloseTimeout |  | ../chromium/src/chromecast/base/chromecast_switches.cc |
| --alsa-enable-upsampling |  Flag that enables resampling audio with sample rate below 32kHz up to 48kHz.  Should be set to true for internal audio products. | kAlsaEnableUpsampling |  | ../chromium/src/chromecast/base/chromecast_switches.cc |
| --alsa-fixed-output-sample-rate |  Optional flag to set a fixed sample rate for the alsa device.  Deprecated: Use --audio-output-sample-rate instead. | kAlsaFixedOutputSampleRate |  | ../chromium/src/chromecast/base/chromecast_switches.cc |
| --alsa-mute-device-name |  Name of the device the mute mixer should be opened on. If this flag is not  specified it will default to the same device as kAlsaVolumeDeviceName. | kAlsaMuteDeviceName |  | ../chromium/src/chromecast/base/chromecast_switches.cc |
| --alsa-mute-element-name |  Name of the simple mixer control element that the ALSA-based media library  should use to mute the system. | kAlsaMuteElementName |  | ../chromium/src/chromecast/base/chromecast_switches.cc |
| --alsa-output-avail-min |  Minimum number of available frames for scheduling a transfer. | kAlsaOutputAvailMin |  | ../chromium/src/chromecast/base/chromecast_switches.cc |
| --alsa-output-buffer-size |  Size of the ALSA output buffer in frames. This directly sets the latency of  the output device. Latency can be calculated by multiplying the sample rate  by the output buffer size. | kAlsaOutputBufferSize |  | ../chromium/src/chromecast/base/chromecast_switches.cc |
| --alsa-output-period-size |  Size of the ALSA output period in frames. The period of an ALSA output device  determines how many frames elapse between hardware interrupts. | kAlsaOutputPeriodSize |  | ../chromium/src/chromecast/base/chromecast_switches.cc |
| --alsa-output-start-threshold |  How many frames need to be in the output buffer before output starts. | kAlsaOutputStartThreshold |  | ../chromium/src/chromecast/base/chromecast_switches.cc |
| --alsa-volume-device-name |  Name of the device the volume control mixer should be opened on. Will use the  same device as kAlsaOutputDevice and fall back to "default" if  kAlsaOutputDevice is not supplied. | kAlsaVolumeDeviceName |  | ../chromium/src/chromecast/base/chromecast_switches.cc |
| --alsa-volume-element-name |  Name of the simple mixer control element that the ALSA-based media library  should use to control the volume. | kAlsaVolumeElementName |  | ../chromium/src/chromecast/base/chromecast_switches.cc |
| --audio-output-channels |  Number of audio output channels. This will be used to send audio buffer with  specific number of channels to ALSA and generate loopback audio. Default  value is 2. | kAudioOutputChannels |  | ../chromium/src/chromecast/base/chromecast_switches.cc |
| --audio-output-sample-rate |  Specify fixed sample rate for audio output stream. If this flag is not  specified the StreamMixer will choose sample rate based on the sample rate of  the media stream. | kAudioOutputSampleRate |  | ../chromium/src/chromecast/base/chromecast_switches.cc |
| --max-output-volume-dba1m |  Calibrated max output volume dBa for voice content at 1 meter, if known. | kMaxOutputVolumeDba1m |  | ../chromium/src/chromecast/base/chromecast_switches.cc |
| --mixer-enable-dynamic-channel-count |  Enable dynamically changing the channel count in the mixer depending on the  input streams. | kMixerEnableDynamicChannelCount |  | ../chromium/src/chromecast/base/chromecast_switches.cc |
| --mixer-source-audio-ready-threshold-ms |  Specify the start threshold frames for audio output when using our mixer.  This is mostly used to override the default value to a larger value, for  platforms that can't handle the default start threshold without running into  audio underruns. | kMixerSourceAudioReadyThresholdMs |  | ../chromium/src/chromecast/base/chromecast_switches.cc |
| --mixer-source-input-queue-ms |  Specify the buffer size for audio output when using our mixer. This is mostly  used to override the default value to a larger value, for platforms that  can't handle an audio buffer so small without running into audio underruns. | kMixerSourceInputQueueMs |  | ../chromium/src/chromecast/base/chromecast_switches.cc |
| --mem-pressure-system-reserved-kb |  Some platforms typically have very little 'free' memory, but plenty is  available in buffers+cached.  For such platforms, configure this amount  as the portion of buffers+cached memory that should be treated as  unavailable.  If this switch is not used, a simple pressure heuristic based  purely on free memory will be used. | kMemPressureSystemReservedKb |  | ../chromium/src/chromecast/base/chromecast_switches.cc |
| --cast-initial-screen-width |  Used to pass initial screen resolution to GPU process.  This allows us to set  screen size correctly (so no need to resize when first window is created). | kCastInitialScreenWidth |  | ../chromium/src/chromecast/base/chromecast_switches.cc |
| --cast-initial-screen-height |  | kCastInitialScreenHeight |  | ../chromium/src/chromecast/base/chromecast_switches.cc |
| --graphics-buffer-count |  | kGraphicsBufferCount |  | ../chromium/src/chromecast/base/chromecast_switches.cc |
| --vsync-interval |  Overrides the vsync interval used by the GPU process to refresh the display. | kVSyncInterval |  | ../chromium/src/chromecast/base/chromecast_switches.cc |
| --desktop-window-1080p |  When present, desktop cast_shell will create 1080p window (provided display  resolution is high enough).  Otherwise, cast_shell defaults to 720p. | kDesktopWindow1080p |  | ../chromium/src/chromecast/base/chromecast_switches.cc |
| --force-media-resolution-height |  When present overrides the screen resolution used by CanDisplayType API,  instead of using the values obtained from avsettings. | kForceMediaResolutionHeight |  | ../chromium/src/chromecast/base/chromecast_switches.cc |
| --force-media-resolution-width |  | kForceMediaResolutionWidth |  | ../chromium/src/chromecast/base/chromecast_switches.cc |
| --enable-input |  Enables input event handling by the window manager. | kEnableInput |  | ../chromium/src/chromecast/base/chromecast_switches.cc |
| --cast-app-background-color |  Background color used when Chromium hasn't rendered anything yet. | kCastAppBackgroundColor |  | ../chromium/src/chromecast/base/chromecast_switches.cc |
| --system-gesture-start-width |  The number of pixels from the very left or right of the screen to consider as  a valid origin for the left or right swipe gesture.  Overrides the default  value in cast_system_gesture_handler.cc. | kSystemGestureStartWidth |  | ../chromium/src/chromecast/base/chromecast_switches.cc |
| --system-gesture-start-height |  The number of pixels from the very top or bottom of the screen to consider as  a valid origin for the top or bottom swipe gesture. Overrides the default  value in cast_system_gesture_handler.cc. | kSystemGestureStartHeight |  | ../chromium/src/chromecast/base/chromecast_switches.cc |
| --bottom-gesture-start-height |  The number of pixels up from the bottom of the screen to consider as a valid  origin for a bottom swipe gesture. If set, overrides the value of both the  above system-gesture-start-height flag and the default value in  cast_system_gesture_handler.cc. | kBottomSystemGestureStartHeight |  | ../chromium/src/chromecast/base/chromecast_switches.cc |
| --back-gesture-horizontal-threshold |  The number of pixels from the start of a left swipe gesture to consider as a  'back' gesture. | kBackGestureHorizontalThreshold |  | ../chromium/src/chromecast/base/chromecast_switches.cc |
| --enable-top-drag-gesture |  Whether to enable detection and dispatch of a 'drag from the top' gesture. | kEnableTopDragGesture |  | ../chromium/src/chromecast/base/chromecast_switches.cc |
| --managed-mode |  Whether in hospitality mode | kManagedMode |  | ../chromium/src/chromecast/base/chromecast_switches.cc |
| --mixer-service-endpoint |  Endpoint that the mixer service listens on. This is a path for a UNIX domain  socket (default is /tmp/mixer-service). | kMixerServiceEndpoint |  | ../chromium/src/chromecast/base/chromecast_switches.cc |
| --mixer-service-port |  TCP port that the mixer service listens on on non-Linux platforms.  (default 12854). | kMixerServicePort |  | ../chromium/src/chromecast/base/chromecast_switches.cc |
| --memory-pressure-critical-fraction |  | kCastMemoryPressureCriticalFraction |  | ../chromium/src/chromecast/base/chromecast_switches.cc |
| --memory-pressure-moderate-fraction |  | kCastMemoryPressureModerateFraction |  | ../chromium/src/chromecast/base/chromecast_switches.cc |
| --disable-mojo-renderer |  Rather than use the renderer hosted remotely in the media service, fall back  to the default renderer within content_renderer. Does not change the behavior  of the media service. | kDisableMojoRenderer |  | ../chromium/src/chromecast/base/chromecast_switches.cc |
| --force-mojo-renderer |  Forces the use of the mojo renderer. In other words, the renderer process  will run a mojo renderer and CastRenderer will run in the browser process.  This is necessary for devices that use CastRenderer.   For this flag to have any effect, note that you must build the cast web  runtime with the gn arg "enable_cast_renderer" set to true, and "renderer"  must be included in the list "mojo_media_services".   This flag has lower priority than "disable-mojo-renderer". | kForceMojoRenderer |  | ../chromium/src/chromecast/base/chromecast_switches.cc |
| --force-update-remote-url |  Per-product customization of force update UI remote url, also used in  testing. | kForceUpdateRemoteUrl |  | ../chromium/src/chromecast/base/chromecast_switches.cc |
| --sys-info-file-path |  System info file path. Default is an empty string, which  means that dummy info will be used. | kSysInfoFilePath |  | ../chromium/src/chromecast/base/chromecast_switches.cc |
| --defer-feature-list |  Defer initialization of the base::FeatureList in an external service process,  allowing the process to include its own non-default features. | kDeferFeatureList |  | ../chromium/src/chromecast/base/chromecast_switches.cc |
| --use-cast-browser-pref-config |  Rather than share a common pref config file with cast_service, use a  dedicated browser pref config file. This must be set when `cast_browser` is  running in a different process from `cast_service`. | kUseCastBrowserPrefConfig |  | ../chromium/src/chromecast/base/chromecast_switches.cc |
| --in-process-broker |  Creates the service broker inside of this process. Only one process should  host the service broker. | kInProcessBroker |  | ../chromium/src/chromecast/base/chromecast_switches.cc |
| --cast-mojo-broker-path |  Command-line arg to change the Unix domain socket path to connect to the  Cast Mojo broker. | kCastMojoBrokerPath |  | ../chromium/src/chromecast/base/chromecast_switches.cc |
| switch | description | variable | cpp condition | location |
| ------ | ----------- | -------- | ------------- | -------- |
| switch | description | variable | cpp condition | location |
| ------ | ----------- | -------- | ------------- | -------- |
| --connectivity-check-url |  Url for network connectivity checking. Default is  "https:clients3.google.com/generate_204". | kConnectivityCheckUrl |  | ../chromium/src/chromecast/net/net_switches.cc |
| --netifs-to-ignore |  List of network interfaces to ignore. Ignored interfaces will not be used  for network connectivity. | kNetifsToIgnore |  | ../chromium/src/chromecast/net/net_switches.cc |
| switch | description | variable | cpp condition | location |
| ------ | ----------- | -------- | ------------- | -------- |
| --force-assistant-onboarding |  | kForceAssistantOnboarding |  | ../chromium/src/chromeos/ash/services/assistant/public/cpp/switches.cc |
| --redirect-libassistant-logging |  | kRedirectLibassistantLogging |  | ../chromium/src/chromeos/ash/services/assistant/public/cpp/switches.cc |
| --disable-libassistant-logfile |  | kDisableLibAssistantLogfile |  | ../chromium/src/chromeos/ash/services/assistant/public/cpp/switches.cc |
| switch | description | variable | cpp condition | location |
| ------ | ----------- | -------- | ------------- | -------- |
| --cryptauth-http-host |  Overrides the default URL for Google APIs (https:www.googleapis.com) used  by CryptAuth. | kCryptAuthHTTPHost |  | ../chromium/src/chromeos/ash/services/device_sync/switches.cc |
| --cryptauth-v2-enrollment-http-host |  Overrides the default URL for CryptAuth v2 Enrollment:  https:cryptauthenrollment.googleapis.com. | kCryptAuthV2EnrollmentHTTPHost |  | ../chromium/src/chromeos/ash/services/device_sync/switches.cc |
| --cryptauth-v2-devicesync-http-host |  Overrides the default URL for CryptAuth v2 DeviceSync:  https:cryptauthdevicesync.googleapis.com. | kCryptAuthV2DeviceSyncHTTPHost |  | ../chromium/src/chromeos/ash/services/device_sync/switches.cc |
| switch | description | variable | cpp condition | location |
| ------ | ----------- | -------- | ------------- | -------- |
| --use-fake-mahi-manager |  Use the fake MahiManager within the Mahi feature. Also always show the Mahi  menu when context menu is shown. | kUseFakeMahiManager |  | ../chromium/src/chromeos/components/mahi/public/cpp/mahi_switches.cc |
| switch | description | variable | cpp condition | location |
| ------ | ----------- | -------- | ------------- | -------- |
| --container-app-preinstall-activation-time-threshold |  The name for the command-line switch used to provide the activation time  threshold for the container app. Note that this switch will only be used for  testing purposes. | kContainerAppPreinstallActivationTimeThreshold |  | ../chromium/src/chromeos/constants/chromeos_switches.cc |
| --container-app-preinstall-debug-key |  The name for the command-line switch used to provide the key which gates  debugging preinstallation of the container app. | kContainerAppPreinstallDebugKey |  | ../chromium/src/chromeos/constants/chromeos_switches.cc |
| --mahi-restrictions-override |  Use in test to override mahi age and country restriction. | kMahiRestrictionsOverride |  | ../chromium/src/chromeos/constants/chromeos_switches.cc |
| switch | description | variable | cpp condition | location |
| ------ | ----------- | -------- | ------------- | -------- |
| --attestation-server |  Used in AttestationClient to determine which Google Privacy CA to use for  attestation. | kAttestationServer |  | ../chromium/src/chromeos/dbus/constants/dbus_switches.cc |
| --biod-fake |  Enables BIOD fake behavior. If the switch is set, fake biod D-Bus client is  initialized and BIOD events do not reach chrome. | kBiodFake |  | ../chromium/src/chromeos/dbus/constants/dbus_switches.cc |
| --cros-disks-fake |  Enables cros disks fake behavior. If the switch is set, fake cros disk D-Bus  client is initialized and USB events do not reach chrome. | kCrosDisksFake |  | ../chromium/src/chromeos/dbus/constants/dbus_switches.cc |
| --dbus-stub |  Forces the stub implementation of D-Bus clients.  Using stub D-Bus clients is the default for non-Chrome OS environment, to use  real D-Bus clients in non-Chrome OS environment, set this flag to "never". | kDbusStub |  | ../chromium/src/chromeos/dbus/constants/dbus_switches.cc |
| --fake-oobe-configuration-file |  Path to a OOBE configuration JSON file (used by FakeOobeConfigurationClient). | kFakeOobeConfiguration |  | ../chromium/src/chromeos/dbus/constants/dbus_switches.cc |
| --shill-stub |  Overrides Shill stub behavior. By default, ethernet, wifi and vpn are  enabled, and transitions occur instantaneously. Multiple options can be  comma separated (no spaces). Note: all options are in the format 'foo=x'.  Values are case sensitive and based on Shill names in service_constants.h.  See FakeShillManagerClient::SetInitialNetworkState for implementation.  Examples:   'clear=1' - Clears all default configurations   'wifi=on' - A wifi network is initially connected ('1' also works)   'wifi=off' - Wifi networks are all initially disconnected ('0' also works)   'wifi=disabled' - Wifi is initially disabled   'wifi=none' - Wifi is unavailable   'wifi=portal' - Wifi connection will be in Portal state   'cellular=1' - Cellular is initially connected   'cellular=LTE' - Cellular is initially connected, technology is LTE   'interactive=3' - Interactive mode, connect/scan/etc requests take 3 secs | kShillStub |  | ../chromium/src/chromeos/dbus/constants/dbus_switches.cc |
| --hermes-fake |  Enables Hermes fake behavior. By default, no carrier profiles are setup.  If a value of "on" is passed for this switch, then hermes fakes are  initialized with a single installed carrier profile. Fake cellular service  corresponding to carrier profiles are also setup in Shill. | kHermesFake |  | ../chromium/src/chromeos/dbus/constants/dbus_switches.cc |
| --sms-test-messages |  Sends test messages on first call to RequestUpdate (stub only). | kSmsTestMessages |  | ../chromium/src/chromeos/dbus/constants/dbus_switches.cc |
| --system-developer-mode |  Used by FakeDebugDaemonClient to specify that the system is running in dev  mode when running in a Linux environment. The dev mode probing is done by  session manager. | kSystemDevMode |  | ../chromium/src/chromeos/dbus/constants/dbus_switches.cc |
| --register-max-dark-suspend-delay |  Makes Chrome register the maximum dark suspend delay possible on Chrome OS  i.e. give the device the maximum amount of time to do its work in dark  resume as is allowed by the power manager. | kRegisterMaxDarkSuspendDelay |  | ../chromium/src/chromeos/dbus/constants/dbus_switches.cc |
| switch | description | variable | cpp condition | location |
| ------ | ----------- | -------- | ------------- | -------- |
| --ondevice_handwriting |  Used to determine if and how on-device handwriting recognition is supported  (e.g. via rootfs or downloadable content). | kOndeviceHandwritingSwitch |  | ../chromium/src/chromeos/services/machine_learning/public/cpp/ml_switches.cc |
| switch | description | variable | cpp condition | location |
| ------ | ----------- | -------- | ------------- | -------- |
| --cros-startup-data-fd |  FD pointing a (memory backed) file containing the startup data. | kCrosStartupDataFD |  | ../chromium/src/chromeos/startup/startup_switches.cc |
| --cros-postlogin-data-fd |  FD pointing to an anonymous pipe containing the post-login data. | kCrosPostLoginDataFD |  | ../chromium/src/chromeos/startup/startup_switches.cc |
| --cros-postlogin-log-file |  The path of the log file that Lacros should use post-login. | kCrosPostLoginLogFile |  | ../chromium/src/chromeos/startup/startup_switches.cc |
| switch | description | variable | cpp condition | location |
| ------ | ----------- | -------- | ------------- | -------- |
| --autofill-api-key |  Sets the API key that will be used when calling Autofill API instead of  using Chrome's baked key by default. You can use this to test new versions  of the API that are not linked to the Chrome baked key yet. | kAutofillAPIKey |  | ../chromium/src/components/autofill/core/common/autofill_switches.cc |
| --autofill-server-url |  Override the default autofill server URL with "scheme:host[:port]/prefix/". | kAutofillServerURL |  | ../chromium/src/components/autofill/core/common/autofill_switches.cc |
| --autofill-upload-throttling-period-in-days |  The number of days after which to reset the registry of autofill events for  which an upload has been sent. | kAutofillUploadThrottlingPeriodInDays |  | ../chromium/src/components/autofill/core/common/autofill_switches.cc |
| --ignore-autocomplete-off-autofill |  Ignores autocomplete="off" for Autofill data (profiles + credit cards). | kIgnoreAutocompleteOffForAutofill |  | ../chromium/src/components/autofill/core/common/autofill_switches.cc |
| --show-autofill-type-predictions |  Annotates forms with Autofill field type predictions. | kShowAutofillTypePredictions |  | ../chromium/src/components/autofill/core/common/autofill_switches.cc |
| --show-autofill-signatures |  Annotates forms and fields with Autofill signatures. | kShowAutofillSignatures |  | ../chromium/src/components/autofill/core/common/autofill_switches.cc |
| --wallet-service-use-sandbox |  Use the sandbox Online Wallet service URL (for developer testing). | kWalletServiceUseSandbox |  | ../chromium/src/components/autofill/core/common/autofill_switches.cc |
| switch | description | variable | cpp condition | location |
| ------ | ----------- | -------- | ------------- | -------- |
| switch | description | variable | cpp condition | location |
| ------ | ----------- | -------- | ------------- | -------- |
| --initialize-client-hints-storage |  Pre-load the client hint storage. Takes a JSON dict, with each key being an  origin (RFC 6454 Section 6.2) and each value a comma-separated list of client  hint tokens (RFC 8942 Section 3.1, client-hints-infrastructure Section 7.1).   Each origin/token-list entry will be parsed and persisted to the Client Hints  storage as though the token-list had come through an Accept-CH response  header from a navigation from the origin.   The initialization will only apply to non-OffTheRecord profiles, meaning  incognito or guest profiles will not have the storage applied. | kInitializeClientHintsStorage |  | ../chromium/src/components/client_hints/common/switches.cc |
| switch | description | variable | cpp condition | location |
| ------ | ----------- | -------- | ------------- | -------- |
| --component-updater |  Comma-separated options to troubleshoot the component updater. Only valid  for the browser process. | kComponentUpdater |  | ../chromium/src/components/component_updater/component_updater_switches.cc |
| --component-updater-trust-tokens-component-path |  Optional testing override of the Trust Tokens key commitment component's  path. | kComponentUpdaterTrustTokensComponentPath |  | ../chromium/src/components/component_updater/component_updater_switches.cc |
| --campaigns-test-tag |  Switch to control which serving campaigns file versions to select in test  cohort. Example: `--campaigns-test-tag=dev1` will select test cohort which  tag matches dev1. | kCampaignsTestTag |  | ../chromium/src/components/component_updater/component_updater_switches.cc |
| --demo-app-test-tag |  Switch to control which serving demo mode app versions to select in test  cohort. Example: `--demo-app-test-tag=dev1` will select test cohort which tag  matches dev1. | kDemoModeTestTag |  | ../chromium/src/components/component_updater/component_updater_switches.cc |
| switch | description | variable | cpp condition | location |
| ------ | ----------- | -------- | ------------- | -------- |
| --crashpad-handler |  A process type (switches::kProcessType) that indicates chrome.exe or  setup.exe is being launched as crashpad_handler. This is only used on  Windows. We bundle the handler into chrome.exe on Windows because there is  high probability of a "new" .exe being blocked or interfered with by  application firewalls, AV software, etc. On other platforms, crashpad_handler  is a standalone executable. | kCrashpadHandler |  | ../chromium/src/components/crash/core/app/crash_switches.cc |
| --crashpad-handler-pid |  The process ID of the Crashpad handler. | kCrashpadHandlerPid | BUILDFLAG(IS_LINUX) || BUILDFLAG(IS_CHROMEOS) | ../chromium/src/components/crash/core/app/crash_switches.cc |
| --crash-loop-before |  A time_t. Passed by session_manager into the Chrome user session, indicating  that if Chrome crashes before the indicated time, session_manager will  consider this to be a crash-loop situation and log the user out. Chrome  mostly just passes this to crash_reporter if it crashes. | kCrashLoopBefore | BUILDFLAG(IS_CHROMEOS_ASH) | ../chromium/src/components/crash/core/app/crash_switches.cc |
| switch | description | variable | cpp condition | location |
| ------ | ----------- | -------- | ------------- | -------- |
| --enable-distillability-service |  | kEnableDistillabilityService |  | ../chromium/src/components/dom_distiller/core/dom_distiller_switches.cc |
| --enable-dom-distiller |  | kEnableDomDistiller |  | ../chromium/src/components/dom_distiller/core/dom_distiller_switches.cc |
| --reader-mode-heuristics |  | kReaderModeHeuristics |  | ../chromium/src/components/dom_distiller/core/dom_distiller_switches.cc |
| --reader-mode-feedback |  | kReaderModeFeedback |  | ../chromium/src/components/dom_distiller/core/dom_distiller_switches.cc |
| --discoverability |  namespace reader_mode_heuristics | kReaderModeDiscoverabilityParamName |  | ../chromium/src/components/dom_distiller/core/dom_distiller_switches.cc |
| --offer-in-settings |  | kReaderModeOfferInSettings |  | ../chromium/src/components/dom_distiller/core/dom_distiller_switches.cc |
| switch | description | variable | cpp condition | location |
| ------ | ----------- | -------- | ------------- | -------- |
| switch | description | variable | cpp condition | location |
| ------ | ----------- | -------- | ------------- | -------- |
| switch | description | variable | cpp condition | location |
| ------ | ----------- | -------- | ------------- | -------- |
| --disable-dinosaur-easter-egg |  Disables the dinosaur easter egg on the offline interstitial. | kDisableDinosaurEasterEgg |  | ../chromium/src/components/error_page/common/error_page_switches.cc |
| --enable-dinosaur-easter-egg-alt-images |  Enable the dinosaur easter egg alternative images. | kEnableDinosaurEasterEggAltGameImages |  | ../chromium/src/components/error_page/common/error_page_switches.cc |
| switch | description | variable | cpp condition | location |
| ------ | ----------- | -------- | ------------- | -------- |
| --feedback-server |  Alternative feedback server to use when submitting user feedback | kFeedbackServer |  | ../chromium/src/components/feedback/feedback_switches.cc |
| switch | description | variable | cpp condition | location |
| ------ | ----------- | -------- | ------------- | -------- |
| --flag-switches-begin |  These two flags are added around the switches about:flags adds to the  command line. This is useful to see which switches were added by about:flags  on about:version. They don't have any effect. | kFlagSwitchesBegin |  | ../chromium/src/components/flags_ui/flags_ui_switches.cc |
| --flag-switches-end |  | kFlagSwitchesEnd |  | ../chromium/src/components/flags_ui/flags_ui_switches.cc |
| switch | description | variable | cpp condition | location |
| ------ | ----------- | -------- | ------------- | -------- |
| --google-base-url |  Specifies an alternate URL to use for speaking to Google. Useful for testing. | kGoogleBaseURL |  | ../chromium/src/components/google/core/common/google_switches.cc |
| --ignore-google-port-numbers |  When set, this will ignore the PortPermission passed in the google_util.h  methods and ignore the port numbers. This makes it easier to run tests for  features that use these methods (directly or indirectly) with the  EmbeddedTestServer, which is more representative of production. | kIgnoreGooglePortNumbers |  | ../chromium/src/components/google/core/common/google_switches.cc |
| switch | description | variable | cpp condition | location |
| ------ | ----------- | -------- | ------------- | -------- |
| --default-background-color |  The background color to be used if the page doesn't specify one. Provided as  RGB or RGBA integer value in hex, e.g. 'ff0000ff' for red or '00000000' for  transparent. | kDefaultBackgroundColor |  | ../chromium/src/components/headless/command_handler/headless_command_switches.cc |
| --dump-dom |  Print the serialized DOM (doctype + document.documentElement.outerHTML) to  stdout. | kDumpDom |  | ../chromium/src/components/headless/command_handler/headless_command_switches.cc |
| --print-to-pdf |  Save a PDF file of the loaded page. | kPrintToPDF |  | ../chromium/src/components/headless/command_handler/headless_command_switches.cc |
| --no-pdf-header-footer |  Do not display header and footer in the printed PDF file. | kNoPDFHeaderFooter |  | ../chromium/src/components/headless/command_handler/headless_command_switches.cc |
| --disable-pdf-tagging |  Do not emit tags when printing PDFs. | kDisablePDFTagging |  | ../chromium/src/components/headless/command_handler/headless_command_switches.cc |
| --generate-pdf-document-outline |  Embed the document outline into printed PDFs. | kGeneratePDFDocumentOutline |  | ../chromium/src/components/headless/command_handler/headless_command_switches.cc |
| --screenshot |  Save a screenshot of the loaded page. | kScreenshot |  | ../chromium/src/components/headless/command_handler/headless_command_switches.cc |
| --timeout |  Issues a stop after the specified number of milliseconds.  This cancels all  navigation and causes the DOMContentLoaded event to fire. | kTimeout |  | ../chromium/src/components/headless/command_handler/headless_command_switches.cc |
| --virtual-time-budget |  If set the system waits the specified number of virtual milliseconds before  deeming the page to be ready.  For determinism virtual time does not advance  while there are pending network fetches (i.e no timers will fire). Once all  network fetches have completed, timers fire and if the system runs out of  virtual time is fastforwarded so the next timer fires immediately, until the  specified virtual time budget is exhausted. | kVirtualTimeBudget |  | ../chromium/src/components/headless/command_handler/headless_command_switches.cc |
| switch | description | variable | cpp condition | location |
| ------ | ----------- | -------- | ------------- | -------- |
| --subproc-heap-profiling |  Forces Heap Profiling on for a subprocess. The browser will add this when  the kHeapProfilerCentralControl feature is enabled and the subprocess should  be profiled. | kSubprocessHeapProfiling |  | ../chromium/src/components/heap_profiling/in_process/switches.cc |
| switch | description | variable | cpp condition | location |
| ------ | ----------- | -------- | ------------- | -------- |
| --validate-input-event-stream |  In debug builds, asserts that the stream of input events is valid. | kValidateInputEventStream |  | ../chromium/src/components/input/switches.cc |
| switch | description | variable | cpp condition | location |
| ------ | ----------- | -------- | ------------- | -------- |
| switch | description | variable | cpp condition | location |
| ------ | ----------- | -------- | ------------- | -------- |
| switch | description | variable | cpp condition | location |
| ------ | ----------- | -------- | ------------- | -------- |
| switch | description | variable | cpp condition | location |
| ------ | ----------- | -------- | ------------- | -------- |
| --cast-developer-certificate-path |  When enabled by build flags, passing this argument allows the Cast  authentication utils to use a custom root developer certificate in the trust  store instead of the root Google-signed cert. | kCastDeveloperCertificatePath |  | ../chromium/src/components/media_router/common/providers/cast/certificate/switches.cc |
| --cast-log-device-cert-chain |  When enabled, prints a PEM-encoded the device certificate chain at VLOG  level 3. | kCastLogDeviceCertChain |  | ../chromium/src/components/media_router/common/providers/cast/certificate/switches.cc |
| switch | description | variable | cpp condition | location |
| ------ | ----------- | -------- | ------------- | -------- |
| --export-uma-logs-to-file |  Enables the observing of all UMA logs created during the session and  automatically exports them to the passed file path on shutdown (the file is  created if it does not already exist). This also enables viewing all UMA logs  in the chrome:metrics-internals debug page. The format of the exported file  is outlined in MetricsServiceObserver::ExportLogsAsJson().  Example usage: --export-uma-logs-to-file=/tmp/logs.json | kExportUmaLogsToFile |  | ../chromium/src/components/metrics/metrics_switches.cc |
| --force-enable-metrics-reporting |  Forces metrics reporting to be enabled. Should not be used for tests as it  will send data to servers. | kForceEnableMetricsReporting |  | ../chromium/src/components/metrics/metrics_switches.cc |
| --force-msbb-setting-on-for-ukm |  Forces MSBB setting to be on for UKM recording. Should only be used in  automated testing browser sessions in which it is infeasible or impractical  to toggle the setting manually. | kForceMsbbSettingOnForUkm |  | ../chromium/src/components/metrics/metrics_switches.cc |
| --metrics-recording-only |  Enables the recording of metrics reports but disables reporting. In contrast  to kForceEnableMetricsReporting, this executes all the code that a normal  client would use for reporting, except the report is dropped rather than sent  to the server. This is useful for finding issues in the metrics code during  UI and performance tests. | kMetricsRecordingOnly |  | ../chromium/src/components/metrics/metrics_switches.cc |
| --metrics-upload-interval |  Override the standard time interval between each metrics report upload for  UMA and UKM. It is useful to set to a short interval for debugging. Unit in  seconds. (The default is 1800 seconds on desktop). | kMetricsUploadIntervalSec |  | ../chromium/src/components/metrics/metrics_switches.cc |
| --reset-variation-state |  Forces a reset of the one-time-randomized FieldTrials on this client, also  known as the Chrome Variations state. | kResetVariationState |  | ../chromium/src/components/metrics/metrics_switches.cc |
| --ukm-server-url |  Overrides the URL of the server that UKM reports are uploaded to. This can  only be used in debug builds. | kUkmServerUrl |  | ../chromium/src/components/metrics/metrics_switches.cc |
| --uma-server-url |  Overrides the URL of the server that UMA reports are uploaded to. This can  only be used in debug builds. | kUmaServerUrl |  | ../chromium/src/components/metrics/metrics_switches.cc |
| --uma-insecure-server-url |  Overrides the URL of the server that UMA reports are uploaded to when the  connection to the default secure URL fails (see |kUmaServerUrl|). This can  only be used in debug builds. | kUmaInsecureServerUrl |  | ../chromium/src/components/metrics/metrics_switches.cc |
| switch | description | variable | cpp condition | location |
| ------ | ----------- | -------- | ------------- | -------- |
| --disable-pnacl-crash-throttling |  Disables crash throttling for Portable Native Client. | kDisablePnaclCrashThrottling |  | ../chromium/src/components/nacl/common/nacl_switches.cc |
| --enable-nacl-debug |  Enables debugging via RSP over a socket. | kEnableNaClDebug |  | ../chromium/src/components/nacl/common/nacl_switches.cc |
| --force-pnacl-subzero |  Force use of the Subzero as the PNaCl translator instead of LLC. | kForcePNaClSubzero |  | ../chromium/src/components/nacl/common/nacl_switches.cc |
| --nacl-debug-mask |  Uses NaCl manifest URL to choose whether NaCl program will be debugged by  debug stub.  Switch value format: [!]pattern1,pattern2,...,patternN. Each pattern uses  the same syntax as patterns in Chrome extension manifest. The only difference  is that * scheme matches all schemes instead of matching only http and https.  If the value doesn't start with !, a program will be debugged if manifest URL  matches any pattern. If the value starts with !, a program will be debugged  if manifest URL does not match any pattern. | kNaClDebugMask |  | ../chromium/src/components/nacl/common/nacl_switches.cc |
| --nacl-gdb-script |  GDB script to pass to the nacl-gdb debugger at startup. | kNaClGdbScript |  | ../chromium/src/components/nacl/common/nacl_switches.cc |
| --nacl-gdb |  Native Client GDB debugger that will be launched automatically when needed. | kNaClGdb |  | ../chromium/src/components/nacl/common/nacl_switches.cc |
| --nacl-loader |  Value for --type that causes the process to run as a NativeClient loader  for SFI mode. | kNaClLoaderProcess |  | ../chromium/src/components/nacl/common/nacl_switches.cc |
| --verbose-logging-in-nacl |  Sets NACLVERBOSITY to enable verbose logging.  This should match the string used in chrome/browser/about_flags.cc | kVerboseLoggingInNacl |  | ../chromium/src/components/nacl/common/nacl_switches.cc |
| --1 |  | kVerboseLoggingInNaclChoiceLow |  | ../chromium/src/components/nacl/common/nacl_switches.cc |
| --2 |  | kVerboseLoggingInNaclChoiceMedium |  | ../chromium/src/components/nacl/common/nacl_switches.cc |
| --4 |  | kVerboseLoggingInNaclChoiceHigh |  | ../chromium/src/components/nacl/common/nacl_switches.cc |
| --7 |  | kVerboseLoggingInNaclChoiceHighest |  | ../chromium/src/components/nacl/common/nacl_switches.cc |
| --0 |  | kVerboseLoggingInNaclChoiceDisabled |  | ../chromium/src/components/nacl/common/nacl_switches.cc |
| switch | description | variable | cpp condition | location |
| ------ | ----------- | -------- | ------------- | -------- |
| --http2-grease-settings |  `kEnableHttp2GreaseSettings` does not include the word "enable" for  historical reasons. | kEnableHttp2GreaseSettings |  | ../chromium/src/components/network_session_configurator/common/network_switches.cc |
| --disable-http2-grease-settings |  | kDisableHttp2GreaseSettings |  | ../chromium/src/components/network_session_configurator/common/network_switches.cc |
| switch | description | variable | cpp condition | location |
| ------ | ----------- | -------- | ------------- | -------- |
| --enable-ntp-search-engine-country-detection |  Enables using the default search engine country to show country specific  popular sites on the NTP. | kEnableNTPSearchEngineCountryDetection |  | ../chromium/src/components/ntp_tiles/switches.cc |
| switch | description | variable | cpp condition | location |
| ------ | ----------- | -------- | ------------- | -------- |
| switch | description | variable | cpp condition | location |
| ------ | ----------- | -------- | ------------- | -------- |
| --optimization_guide_hints_override |  Overrides the Hints Protobuf that would come from the component updater. If  the value of this switch is invalid, regular hint processing is used.  The value of this switch should be a base64 encoding of a binary  Configuration message, found in optimization_guide's hints.proto. Providing a  valid value to this switch causes Chrome startup to block on hints parsing. | kHintsProtoOverride |  | ../chromium/src/components/optimization_guide/core/optimization_guide_switches.cc |
| --optimization-guide-fetch-hints-override |  Overrides scheduling and time delays for fetching hints and causes a hints  fetch immediately on start up using the provided comma separate lists of  hosts. | kFetchHintsOverride |  | ../chromium/src/components/optimization_guide/core/optimization_guide_switches.cc |
| --optimization-guide-fetch-hints-override-timer |  Overrides the hints fetch scheduling and delay, causing a hints fetch  immediately on start up using the TopHostProvider. This is meant for testing. | kFetchHintsOverrideTimer |  | ../chromium/src/components/optimization_guide/core/optimization_guide_switches.cc |
| --optimization-guide-service-get-hints-url |  Overrides the Optimization Guide Service URL that the HintsFetcher will  request remote hints from. | kOptimizationGuideServiceGetHintsURL |  | ../chromium/src/components/optimization_guide/core/optimization_guide_switches.cc |
| --optimization-guide-service-get-models-url |  Overrides the Optimization Guide Service URL that the PredictionModelFetcher  will request remote models and host features from. | kOptimizationGuideServiceGetModelsURL |  | ../chromium/src/components/optimization_guide/core/optimization_guide_switches.cc |
| --optimization-guide-service-model-execution-url |  Overrides the Optimization Guide model execution URL. | kOptimizationGuideServiceModelExecutionURL |  | ../chromium/src/components/optimization_guide/core/optimization_guide_switches.cc |
| --optimization-guide-service-api-key |  Overrides the Optimization Guide Service API Key for remote requests to be  made. | kOptimizationGuideServiceAPIKey |  | ../chromium/src/components/optimization_guide/core/optimization_guide_switches.cc |
| --purge-optimization-guide-store |  Purges the store containing fetched and component hints on startup, so that  it's guaranteed to be using fresh data. | kPurgeHintsStore |  | ../chromium/src/components/optimization_guide/core/optimization_guide_switches.cc |
| --purge-model-and-features-store |  Purges the store containing prediction medels and host model features on  startup, so that it's guaranteed to be using fresh data. | kPurgeModelAndFeaturesStore |  | ../chromium/src/components/optimization_guide/core/optimization_guide_switches.cc |
| --disable-fetching-hints-at-navigation-start |  | kDisableFetchingHintsAtNavigationStartForTesting |  | ../chromium/src/components/optimization_guide/core/optimization_guide_switches.cc |
| --disable-checking-optimization-guide-user-permissions |  | kDisableCheckingUserPermissionsForTesting |  | ../chromium/src/components/optimization_guide/core/optimization_guide_switches.cc |
| --disable-model-download-verification |  | kDisableModelDownloadVerificationForTesting |  | ../chromium/src/components/optimization_guide/core/optimization_guide_switches.cc |
| --enable-optimization-guide-debug-logs |  | kDebugLoggingEnabled |  | ../chromium/src/components/optimization_guide/core/optimization_guide_switches.cc |
| --optimization-guide-model-override |  Disables the fetching of models and overrides the file path and metadata to  be used for the session to use what's passed via command-line instead of what  is already stored.   We expect that the string be a comma-separated string of model overrides with  each model override be: OPTIMIZATION_TARGET_STRING:file_path or  OPTIMIZATION_TARGET_STRING:file_path:base64_encoded_any_proto_model_metadata.   It is possible this only works on Desktop since file paths are less easily  accessible on Android, but may work. | kModelOverride |  | ../chromium/src/components/optimization_guide/core/optimization_guide_switches.cc |
| --optimization-guide-ondevice-model-execution-override |  Overrides the on-device model file paths for on-device model execution. | kOnDeviceModelExecutionOverride |  | ../chromium/src/components/optimization_guide/core/optimization_guide_switches.cc |
| --optimization-guide-ondevice-model-adaptations-override |  Overrides the on-device model adaptation file paths for on-device model  execution. | kOnDeviceModelAdaptationsOverride |  | ../chromium/src/components/optimization_guide/core/optimization_guide_switches.cc |
| --ondevice-validation-request-override |  Enables the on-device model to run validation at startup after a delay. A  text file can be provided used as input for the validation job and an output  file path can be provided to write the response to. | kOnDeviceValidationRequestOverride |  | ../chromium/src/components/optimization_guide/core/optimization_guide_switches.cc |
| --ondevice-validation-write-to-file |  | kOnDeviceValidationWriteToFile |  | ../chromium/src/components/optimization_guide/core/optimization_guide_switches.cc |
| --optimization-guide-model-validate |  Triggers validation of the model. Used for manual testing. | kModelValidate |  | ../chromium/src/components/optimization_guide/core/optimization_guide_switches.cc |
| --optimization-guide-model-execution-validate |  Triggers validation of the server-side AI model execution. Used for  integration testing. | kModelExecutionValidate |  | ../chromium/src/components/optimization_guide/core/optimization_guide_switches.cc |
| --model-quality-service-url |  Overrides the model quality service URL. | kModelQualityServiceURL |  | ../chromium/src/components/optimization_guide/core/optimization_guide_switches.cc |
| --model-quality-service-api-key |  Overrides the ModelQuality Service API Key for remote requests to be made. | kModelQualityServiceAPIKey |  | ../chromium/src/components/optimization_guide/core/optimization_guide_switches.cc |
| --enable-model-quality-dogfood-logging |  Enables model quality logs regardless of other client-side settings, as long  as the client is a dogfood client. | kEnableModelQualityDogfoodLogging |  | ../chromium/src/components/optimization_guide/core/optimization_guide_switches.cc |
| --optimization-guide-get-free-disk-space-with-user-visible-priority-task |  | kGetFreeDiskSpaceWithUserVisiblePriorityTask |  | ../chromium/src/components/optimization_guide/core/optimization_guide_switches.cc |
| --optimization-guide-language-override |  Allows sending an language code to the backend. | kOptimizationGuideLanguageOverride |  | ../chromium/src/components/optimization_guide/core/optimization_guide_switches.cc |
| --optimization-guide-google-api-key-configuration-check-override |  Enables overriding Google API key configuration check for permissions. | kGoogleApiKeyConfigurationCheckOverride |  | ../chromium/src/components/optimization_guide/core/optimization_guide_switches.cc |
| switch | description | variable | cpp condition | location |
| ------ | ----------- | -------- | ------------- | -------- |
| switch | description | variable | cpp condition | location |
| ------ | ----------- | -------- | ------------- | -------- |
| --use-mock-keychain |  | kUseMockKeychain | BUILDFLAG(IS_APPLE) | ../chromium/src/components/os_crypt/sync/os_crypt_switches.cc |
| switch | description | variable | cpp condition | location |
| ------ | ----------- | -------- | ------------- | -------- |
| --enable-page-content-annotations-logging |  | kPageContentAnnotationsLoggingEnabled |  | ../chromium/src/components/page_content_annotations/core/page_content_annotations_switches.cc |
| --page-content-annotations-validation-startup-delay-seconds |  | kPageContentAnnotationsValidationStartupDelaySeconds |  | ../chromium/src/components/page_content_annotations/core/page_content_annotations_switches.cc |
| --page-content-annotations-validation-batch-size |  | kPageContentAnnotationsValidationBatchSizeOverride |  | ../chromium/src/components/page_content_annotations/core/page_content_annotations_switches.cc |
| --page-content-annotations-validation-content-visibility |  Enables the specific annotation type to run validation at startup after a  delay. A comma separated list of inputs can be given as a value which will be  used as input for the validation job. | kPageContentAnnotationsValidationContentVisibility |  | ../chromium/src/components/page_content_annotations/core/page_content_annotations_switches.cc |
| --page-content-annotations-validation-write-to-file |  Writes the output of page content annotation validations to the given file. | kPageContentAnnotationsValidationWriteToFile |  | ../chromium/src/components/page_content_annotations/core/page_content_annotations_switches.cc |
| switch | description | variable | cpp condition | location |
| ------ | ----------- | -------- | ------------- | -------- |
| switch | description | variable | cpp condition | location |
| ------ | ----------- | -------- | ------------- | -------- |
| --deny-permission-prompts |  Prevents permission prompts from appearing by denying instead of showing  prompts. | kDenyPermissionPrompts |  | ../chromium/src/components/permissions/switches.cc |
| switch | description | variable | cpp condition | location |
| ------ | ----------- | -------- | ------------- | -------- |
| --device-management-url |  Specifies the URL at which to communicate with the device management backend  to fetch configuration policies and perform other device tasks. | kDeviceManagementUrl |  | ../chromium/src/components/policy/core/common/policy_switches.cc |
| --realtime-reporting-url |  Specifies the URL at which to upload real-time reports. | kRealtimeReportingUrl |  | ../chromium/src/components/policy/core/common/policy_switches.cc |
| --encrypted-reporting-url |  Specifies the URL at which to upload encrypted reports. | kEncryptedReportingUrl |  | ../chromium/src/components/policy/core/common/policy_switches.cc |
| --policy |  Set policy value by command line. | kChromePolicy |  | ../chromium/src/components/policy/core/common/policy_switches.cc |
| --file-storage-server-upload-url |  Specifies the URL at which to communicate with File Storage Server  (go/crosman-file-storage-server) to upload log and support packet files. | kFileStorageServerUploadUrl |  | ../chromium/src/components/policy/core/common/policy_switches.cc |
| --policy-verification-key |  Replace the original verification_key with the one provided by the command  line flag. Can be used only for unit tests or browser tests. | kPolicyVerificationKey |  | ../chromium/src/components/policy/core/common/policy_switches.cc |
| --disable-policy-key-verification |  Disables the verification of policy signing keys. It just works on Chrome OS  test images and crashes otherwise.  TODO(crbug.com/1225054): This flag might introduce security risks. Find a  better solution to enable policy tast test for Family Link account. | kDisablePolicyKeyVerification | BUILDFLAG(IS_CHROMEOS_ASH) | ../chromium/src/components/policy/core/common/policy_switches.cc |
| --secure-connect-api-url |  Specifies the base URL to contact the secure connect Api. | kSecureConnectApiUrl |  | ../chromium/src/components/policy/core/common/policy_switches.cc |
| switch | description | variable | cpp condition | location |
| ------ | ----------- | -------- | ------------- | -------- |
| switch | description | variable | cpp condition | location |
| ------ | ----------- | -------- | ------------- | -------- |
| --mark_as_phishing |  List of comma-separated URLs to show the social engineering red interstitial  for. | kMarkAsPhishing |  | ../chromium/src/components/safe_browsing/core/common/safebrowsing_switches.cc |
| --safebrowsing-manual-download-blacklist |  List of comma-separated sha256 hashes of executable files which the  download-protection service should treat as "dangerous."  For a file to  show a warning, it also must be considered a dangerous filetype and not  be allowlisted otherwise (by signature or URL) and must be on a supported  OS. Hashes are in hex. This is used for manual testing when looking  for ways to by-pass download protection. | kSbManualDownloadBlocklist |  | ../chromium/src/components/safe_browsing/core/common/safebrowsing_switches.cc |
| --safebrowsing-enable-enhanced-protection |  Enable Safe Browsing Enhanced Protection. | kSbEnableEnhancedProtection |  | ../chromium/src/components/safe_browsing/core/common/safebrowsing_switches.cc |
| switch | description | variable | cpp condition | location |
| ------ | ----------- | -------- | ------------- | -------- |
| --extra-search-query-params |  | kExtraSearchQueryParams |  | ../chromium/src/components/search_engines/search_engines_switches.cc |
| --search-engine-choice-country |  | kSearchEngineChoiceCountry |  | ../chromium/src/components/search_engines/search_engines_switches.cc |
| --ignore-no-first-run-for-search-engine-choice-screen |  | kIgnoreNoFirstRunForSearchEngineChoiceScreen |  | ../chromium/src/components/search_engines/search_engines_switches.cc |
| --disable-search-engine-choice-screen |  | kDisableSearchEngineChoiceScreen |  | ../chromium/src/components/search_engines/search_engines_switches.cc |
| --force-search-engine-choice-screen |  | kForceSearchEngineChoiceScreen |  | ../chromium/src/components/search_engines/search_engines_switches.cc |
| switch | description | variable | cpp condition | location |
| ------ | ----------- | -------- | ------------- | -------- |
| --google-doodle-url |  Overrides the URL used to fetch the current Google Doodle.  Example: https:www.google.com/async/ddljson  Testing? Try:    https:www.gstatic.com/chrome/ntp/doodle_test/ddljson_android0.json    https:www.gstatic.com/chrome/ntp/doodle_test/ddljson_android1.json    https:www.gstatic.com/chrome/ntp/doodle_test/ddljson_android2.json    https:www.gstatic.com/chrome/ntp/doodle_test/ddljson_android3.json    https:www.gstatic.com/chrome/ntp/doodle_test/ddljson_android4.json | kGoogleDoodleUrl |  | ../chromium/src/components/search_provider_logos/switches.cc |
| --search-provider-logo-url |  Use a static URL for the logo of the default search engine.  Example: https:www.google.com/branding/logo.png | kSearchProviderLogoURL |  | ../chromium/src/components/search_provider_logos/switches.cc |
| --third-party-doodle-url |  Overrides the Doodle URL to use for third-party search engines.  Testing? Try:    https:www.gstatic.com/chrome/ntp/doodle_test/third_party_simple.json    https:www.gstatic.com/chrome/ntp/doodle_test/third_party_animated.json | kThirdPartyDoodleURL |  | ../chromium/src/components/search_provider_logos/switches.cc |
| switch | description | variable | cpp condition | location |
| ------ | ----------- | -------- | ------------- | -------- |
| switch | description | variable | cpp condition | location |
| ------ | ----------- | -------- | ------------- | -------- |
| switch | description | variable | cpp condition | location |
| ------ | ----------- | -------- | ------------- | -------- |
| switch | description | variable | cpp condition | location |
| ------ | ----------- | -------- | ------------- | -------- |
| switch | description | variable | cpp condition | location |
| ------ | ----------- | -------- | ------------- | -------- |
| switch | description | variable | cpp condition | location |
| ------ | ----------- | -------- | ------------- | -------- |
| switch | description | variable | cpp condition | location |
| ------ | ----------- | -------- | ------------- | -------- |
| --force-fre-default-browser-step |  Force enable the default browser step in the first run experience on Desktop. | kForceFreDefaultBrowserStep | BUILDFLAG(ENABLE_DICE_SUPPORT) | ../chromium/src/components/signin/public/base/signin_switches.cc |
| --clear-token-service |  Clears the token service before using it. This allows simulating the  expiration of credentials during testing. | kClearTokenService |  | ../chromium/src/components/signin/public/base/signin_switches.cc |
| switch | description | variable | cpp condition | location |
| ------ | ----------- | -------- | ------------- | -------- |
| switch | description | variable | cpp condition | location |
| ------ | ----------- | -------- | ------------- | -------- |
| switch | description | variable | cpp condition | location |
| ------ | ----------- | -------- | ------------- | -------- |
| --initialize-mojo-as-broker |  Used by some tests to force Mojo broker initialization in a spawned child  process. | kInitializeMojoAsBroker |  | ../chromium/src/components/test/test_switches.cc |
| switch | description | variable | cpp condition | location |
| ------ | ----------- | -------- | ------------- | -------- |
| --enable-background-tracing |  Enables background tracing by passing a scenarios config as an argument. The  config is a serialized proto `perfetto.protos.ChromeFieldTracingConfig`  defined in  third_party/perfetto/protos/perfetto/config/chrome/scenario_config.proto.  protoc can be used to generate a serialized proto config with  protoc    --encode=perfetto.protos.ChromeFieldTracingConfig    --proto_path=third_party/perfetto/      third_party/perfetto/protos/perfetto/config/chrome/scenario_config.proto   < {input txt config}.pbtxt > {output proto config}.pb | kEnableBackgroundTracing |  | ../chromium/src/components/tracing/common/tracing_switches.cc |
| --enable-legacy-background-tracing |  Enables background tracing by passing legacy trigger rules as an argument. | kEnableLegacyBackgroundTracing |  | ../chromium/src/components/tracing/common/tracing_switches.cc |
| --trace-config-file |  Causes TRACE_EVENT flags to be recorded from startup.  This flag will be ignored if --trace-startup or --trace-shutdown is provided. | kTraceConfigFile |  | ../chromium/src/components/tracing/common/tracing_switches.cc |
| --trace-startup |  Causes TRACE_EVENT flags to be recorded from startup. Optionally, can  specify the specific trace categories to include (e.g.  --trace-startup=base,net) otherwise, all events are recorded. Setting this  flag results in the first call to BeginTracing() to receive all trace events  since startup.   Historically, --trace-startup was used for browser startup profiling and  --enable-tracing was used for browsertest tracing. Now they are share the  same implementation, but both are still supported to avoid disrupting  existing workflows. The only difference between them is the default duration  (5 seconds for trace-startup, unlimited for enable-tracing). If both are  specified, 'trace-startup' takes precedence.   In Chrome, you may find --trace-startup-file and  --trace-startup-duration to control the auto-saving of the trace (not  supported in the base-only TraceLog component). | kTraceStartup |  | ../chromium/src/components/tracing/common/tracing_switches.cc |
| --enable-tracing |  | kEnableTracing |  | ../chromium/src/components/tracing/common/tracing_switches.cc |
| --trace-config-handle |  Causes TRACE_EVENT flags to be recorded from startup, passing a SMB  handle containing the serialized perfetto config. This flag will be  ignored if --trace-startup or --trace-shutdown is provided. | kTraceConfigHandle |  | ../chromium/src/components/tracing/common/tracing_switches.cc |
| --trace-startup-duration |  Sets the time in seconds until startup tracing ends. If omitted:  - if --trace-startup is specified, a default of 5 seconds is used.  - if --enable-tracing is specified, tracing lasts until the browser is  closed. Has no effect otherwise. | kTraceStartupDuration |  | ../chromium/src/components/tracing/common/tracing_switches.cc |
| --trace-startup-file |  If supplied, sets the file which startup tracing will be stored into, if  omitted the default will be used "chrometrace.log" in the current directory.  Has no effect unless --trace-startup is also supplied.  Example: --trace-startup --trace-startup-file=/tmp/trace_event.log  As a special case, can be set to 'none' - this disables automatically saving  the result to a file and the first manually recorded trace will then receive  all events since startup. | kTraceStartupFile |  | ../chromium/src/components/tracing/common/tracing_switches.cc |
| --enable-tracing-output |  Similar to the flag above, with the following differences:  - A more detailed basename will be generated.  - If the value is empty or ends with path separator, the provided directory  will be used (with empty standing for current directory) and a detailed  basename file will be generated.   It is ignored if --trace-startup-file is specified. | kEnableTracingOutput |  | ../chromium/src/components/tracing/common/tracing_switches.cc |
| --trace-startup-format |  Sets the output format for the trace, valid values are "json" and "proto".  If not set, the current default is "proto".  "proto", unlike json, supports writing the trace into the output file  incrementally and is more likely to retain more data if the browser process  unexpectedly terminates.  Ignored if "trace-startup-owner" is not "controller". | kTraceStartupFormat |  | ../chromium/src/components/tracing/common/tracing_switches.cc |
| --enable-tracing-format |  | kEnableTracingFormat |  | ../chromium/src/components/tracing/common/tracing_switches.cc |
| --trace-startup-record-mode |  If supplied, sets the tracing record mode and options; otherwise, the default  "record-until-full" mode will be used. | kTraceStartupRecordMode |  | ../chromium/src/components/tracing/common/tracing_switches.cc |
| --trace-startup-owner |  Specifies the coordinator of the startup tracing session. If the legacy  tracing backend is used instead of perfetto, providing this flag is not  necessary. Valid values: 'controller', 'devtools', or 'system'. Defaults to  'controller'.   If 'controller' is specified, the session is controlled and stopped via the  TracingController (e.g. to implement the timeout).   If 'devtools' is specified, the startup tracing session will be owned by  DevTools and thus can be controlled (i.e. stopped) via the DevTools Tracing  domain on the first session connected to the browser endpoint.   If 'system' is specified, the system Perfetto service should already be  tracing on a supported platform (currently only Android). Session is stopped  through the normal methods for stopping system traces. | kTraceStartupOwner |  | ../chromium/src/components/tracing/common/tracing_switches.cc |
| --perfetto-disable-interning |  Repeat internable data for each TraceEvent in the perfetto proto format. | kPerfettoDisableInterning |  | ../chromium/src/components/tracing/common/tracing_switches.cc |
| --trace-to-console |  Sends a pretty-printed version of tracing info to the console. | kTraceToConsole |  | ../chromium/src/components/tracing/common/tracing_switches.cc |
| --background-tracing-output-path |  Sets a local folder destination for tracing data. This is only used if  kEnableBackgroundTracing is also specified. | kBackgroundTracingOutputPath |  | ../chromium/src/components/tracing/common/tracing_switches.cc |
| --trace-smb-size |  Configures the size of the shared memory buffer used for tracing. Value is  provided in kB. Defaults to 4096. Should be a multiple of the SMB page size  (currently 32kB on Desktop or 4kB on Android). | kTraceSmbSize |  | ../chromium/src/components/tracing/common/tracing_switches.cc |
| --default-trace-buffer-size-limit-in-kb |  This is only used when we did not set buffer size in trace config and will be  used for all trace sessions. If not provided, we will use the default value  provided in perfetto_config.cc | kDefaultTraceBufferSizeLimitInKb |  | ../chromium/src/components/tracing/common/tracing_switches.cc |
| switch | description | variable | cpp condition | location |
| ------ | ----------- | -------- | ------------- | -------- |
| --translate-script-url |  Overrides the default server used for Google Translate. | kTranslateScriptURL |  | ../chromium/src/components/translate/core/common/translate_switches.cc |
| --translate-security-origin |  Overrides security-origin with which Translate runs in an isolated world. | kTranslateSecurityOrigin |  | ../chromium/src/components/translate/core/common/translate_switches.cc |
| --translate-ranker-model-url |  Overrides the URL from which the translate ranker model is downloaded. | kTranslateRankerModelURL |  | ../chromium/src/components/translate/core/common/translate_switches.cc |
| switch | description | variable | cpp condition | location |
| ------ | ----------- | -------- | ------------- | -------- |
| switch | description | variable | cpp condition | location |
| ------ | ----------- | -------- | ------------- | -------- |
| --enable-ui-devtools |  Enables DevTools server for UI (mus, ash, etc). Value should be the port the  server is started on. Default port is 9223. | kEnableUiDevTools |  | ../chromium/src/components/ui_devtools/switches.cc |
| switch | description | variable | cpp condition | location |
| ------ | ----------- | -------- | ------------- | -------- |
| --disable-field-trial-config |  Disable field trial tests configured in fieldtrial_testing_config.json. | kDisableFieldTrialTestingConfig |  | ../chromium/src/components/variations/variations_switches.cc |
| --disable-variations-safe-mode |  Disable variations safe mode. | kDisableVariationsSafeMode |  | ../chromium/src/components/variations/variations_switches.cc |
| --disable-variations-seed-fetch-throttling |  Disables throttling for fetching the variations seed on mobile platforms. The  seed will be fetched on startup and every time the app enters the foreground,  regardless of the time passed in between the fetches. On Desktop, this switch  has no effect (the seed is fetched periodically instead). | kDisableVariationsSeedFetchThrottling |  | ../chromium/src/components/variations/variations_switches.cc |
| --enable-benchmarking |  TODO(asvitkine): Consider removing or renaming this functionality.  Enables the benchmarking extensions. | kEnableBenchmarking |  | ../chromium/src/components/variations/variations_switches.cc |
| --enable-field-trial-config |  Enable field trial tests configured in fieldtrial_testing_config.json. If the  "disable_fieldtrial_testing_config" GN flag is set to true, then this switch  is a no-op. Otherwise, for non-Chrome branded builds, the testing config is  already applied by default, unless the "--disable-field-trial-config",  "--force-fieldtrials", and/or "--variations-server-url" switches are passed.  It is however possible to apply the testing config as well as specify  additional field trials (using "--force-fieldtrials") by using this switch.  For Chrome-branded builds, the testing config is not enabled by default, so  this switch is required to enable it. | kEnableFieldTrialTestingConfig |  | ../chromium/src/components/variations/variations_switches.cc |
| --fake-variations-channel |  Fakes the channel of the browser for purposes of Variations filtering. This  is to be used for testing only. Possible values are "stable", "beta", "dev"  and "canary". This works for official builds as well. | kFakeVariationsChannel |  | ../chromium/src/components/variations/variations_switches.cc |
| --force-fieldtrial-params |  This option can be used to force parameters of field trials when testing  changes locally. The argument is a param list of (key, value) pairs prefixed  by an associated (trial, group) pair. You specify the param list for multiple  (trial, group) pairs with a comma separator.  Example:    "Trial1.Group1:k1/v1/k2/v2,Trial2.Group2:k3/v3/k4/v4"  Trial names, groups names, parameter names, and value should all be URL  escaped for all non-alphanumeric characters. | kForceFieldTrialParams |  | ../chromium/src/components/variations/variations_switches.cc |
| --force-variation-ids |  Forces additional Chrome Variation Ids that will be sent in X-Client-Data  header, specified as a 64-bit encoded list of numeric experiment ids. Ids  prefixed with the character "t" will be treated as Trigger Variation Ids. | kForceVariationIds |  | ../chromium/src/components/variations/variations_switches.cc |
| --force-disable-variation-ids |  Forces to remove Chrome Variation Ids from being sent in X-Client-Data  header, specified as a 64-bit encoded list of numeric experiment ids. Ids  prefixed with the character "t" will be treated as Trigger Variation Ids. | kForceDisableVariationIds |  | ../chromium/src/components/variations/variations_switches.cc |
| --variations-seed-version |  Used to share variations seed version with child processes. | kVariationsSeedVersion |  | ../chromium/src/components/variations/variations_switches.cc |
| --variations-override-country |  Allows overriding the country used for evaluating variations. This is similar  to the "Override Variations Country" entry on chrome:translate-internals,  but is exposed as a command-line flag to allow testing First Run scenarios.  Additionally, unlike chrome:translate-internals, the value isn't persisted  across sessions. | kVariationsOverrideCountry |  | ../chromium/src/components/variations/variations_switches.cc |
| --variations-test-seed-path |  Specifies the location of a seed file for Local State's seed to be  populated from. The seed file must be in json format with the keys  |kVariationsCompressedSeed| and |kVariationsSeedSignature|. | kVariationsTestSeedJsonPath |  | ../chromium/src/components/variations/variations_switches.cc |
| --variations-server-url |  Specifies a custom URL for the server which reports variation data to the  client. Specifying this switch enables the Variations service on  unofficial builds. See variations_service.cc. | kVariationsServerURL |  | ../chromium/src/components/variations/variations_switches.cc |
| --variations-insecure-server-url |  Specifies a custom URL for the server to use as an insecure fallback when  requests to |kVariationsServerURL| fail. Requests to this URL will be  encrypted. | kVariationsInsecureServerURL |  | ../chromium/src/components/variations/variations_switches.cc |
| --variations-seed-fetch-interval |  Override the time interval between each variation seed fetches. Unit is in  minutes. The minimum is 1 minute. The default is 30 minutes. | kVariationsSeedFetchInterval |  | ../chromium/src/components/variations/variations_switches.cc |
| --enable-finch-seed-delta-compression |  Enables delta-compression when fetching a new seed via the "first run" code  path on Android. | kEnableFinchSeedDeltaCompression |  | ../chromium/src/components/variations/variations_switches.cc |
| --accept-empty-variations-seed-signature |  Accept an empty signature when loading a variations seed. This is for  testing purposes. | kAcceptEmptySeedSignatureForTesting |  | ../chromium/src/components/variations/variations_switches.cc |
| switch | description | variable | cpp condition | location |
| ------ | ----------- | -------- | ------------- | -------- |
| --deadline-to-synchronize-surfaces |  The default number of the BeginFrames to wait to activate a surface with  dependencies. | kDeadlineToSynchronizeSurfaces |  | ../chromium/src/components/viz/common/switches.cc |
| --delegated-ink-renderer |  Force the use of a Delegated Ink renderer as specified by  the command line argument, rather than using system details. Acceptable  values are: skia, system, none. Default to skia. | kDelegatedInkRenderer |  | ../chromium/src/components/viz/common/switches.cc |
| --disable-adpf |  Disables reporting of frame timing via ADPF, even if supported on the device. | kDisableAdpf |  | ../chromium/src/components/viz/common/switches.cc |
| --disable-frame-rate-limit |  Disables begin frame limiting in both cc scheduler and display scheduler.  Also implies --disable-gpu-vsync (see ui/gl/gl_switches.h).  TODO(ananta/jonross/sunnyps)  http:crbug.com/346931323  We should remove or change this once VRR support is implemented for  Windows and other platforms potentially. | kDisableFrameRateLimit |  | ../chromium/src/components/viz/common/switches.cc |
| --double-buffer-compositing |  Sets the number of max pending frames in the GL buffer queue to 1. | kDoubleBufferCompositing |  | ../chromium/src/components/viz/common/switches.cc |
| --enable-hardware-overlays |  Enable compositing individual elements via hardware overlays when  permitted by device.  Setting the flag to "single-fullscreen" will try to promote a single  fullscreen overlay and use it as main framebuffer where possible. | kEnableHardwareOverlays |  | ../chromium/src/components/viz/common/switches.cc |
| --run-all-compositor-stages-before-draw |  Effectively disables pipelining of compositor frame production stages by  waiting for each stage to finish before completing a frame. | kRunAllCompositorStagesBeforeDraw |  | ../chromium/src/components/viz/common/switches.cc |
| --show-aggregated-damage |  Adds a DebugBorderDrawQuad to the top of the root RenderPass showing the  damage rect after surface aggregation. Note that when enabled this feature  sets the entire output rect as damaged after adding the quad to highlight the  real damage rect, which could hide damage rect problems. | kShowAggregatedDamage |  | ../chromium/src/components/viz/common/switches.cc |
| --tint-composited-content-modulate |  Modulates the debug compositor tint color so that damage and page flip  updates are made clearly visible. This feature was useful in determining the  root cause of https:b.corp.google.com/issues/183260320 . The tinting flag  "tint-composited-content" must also be enabled for this flag to used. | kTintCompositedContentModulate |  | ../chromium/src/components/viz/common/switches.cc |
| --show-dc-layer-debug-borders |  Show debug borders for DC layers - red for overlays and blue for underlays.  The debug borders are offset from the layer rect by a few pixels for clarity. | kShowDCLayerDebugBorders |  | ../chromium/src/components/viz/common/switches.cc |
| switch | description | variable | cpp condition | location |
| ------ | ----------- | -------- | ------------- | -------- |
| --viz-demo-use-gpu |  | kVizDemoUseGPU |  | ../chromium/src/components/viz/demo/common/switches.cc |
| switch | description | variable | cpp condition | location |
| ------ | ----------- | -------- | ------------- | -------- |
| --bypass-app-banner-engagement-checks |  This flag causes the user engagement checks for showing app banners to be  bypassed. It is intended to be used by developers who wish to test that their  sites otherwise meet the criteria needed to show app banners. | kBypassAppBannerEngagementChecks |  | ../chromium/src/components/webapps/common/switches.cc |
| --bypass-installable-message-throttle-for-testing |  This flag allow bypassing installable message throttle for testing purpose. | kBypassInstallThrottleForTesting |  | ../chromium/src/components/webapps/common/switches.cc |
| switch | description | variable | cpp condition | location |
| ------ | ----------- | -------- | ------------- | -------- |
| switch | description | variable | cpp condition | location |
| ------ | ----------- | -------- | ------------- | -------- |
| switch | description | variable | cpp condition | location |
| ------ | ----------- | -------- | ------------- | -------- |
| switch | description | variable | cpp condition | location |
| ------ | ----------- | -------- | ------------- | -------- |
| switch | description | variable | cpp condition | location |
| ------ | ----------- | -------- | ------------- | -------- |
| switch | description | variable | cpp condition | location |
| ------ | ----------- | -------- | ------------- | -------- |
| switch | description | variable | cpp condition | location |
| ------ | ----------- | -------- | ------------- | -------- |
| switch | description | variable | cpp condition | location |
| ------ | ----------- | -------- | ------------- | -------- |
| --allow-file-access-from-files |  By default, file: URIs cannot read other file: URIs. This is an  override for developers who need the old behavior for testing. | kAllowFileAccessFromFiles |  | ../chromium/src/content/public/common/content_switches.cc |
| --allow-insecure-localhost |  Enables TLS/SSL errors on localhost to be ignored (no interstitial,  no blocking of requests). | kAllowInsecureLocalhost |  | ../chromium/src/content/public/common/content_switches.cc |
| --allow-loopback-in-peer-connection |  Allows loopback interface to be added in network list for peer connection. | kAllowLoopbackInPeerConnection |  | ../chromium/src/content/public/common/content_switches.cc |
| --allow-command-line-plugins |  Allows plugins to be loaded in the command line for testing. | kAllowCommandLinePlugins |  | ../chromium/src/content/public/common/content_switches.cc |
| --attribution-reporting-debug-mode |  Causes the Attribution Report API to run without delays or noise. | kAttributionReportingDebugMode |  | ../chromium/src/content/public/common/content_switches.cc |
| --auto-accept-camera-and-microphone-capture |  Bypasses the dialog prompting the user for permission to capture  cameras and microphones. Useful in automatic tests of video-conferencing  Web applications.  This is nearly identical to kUseFakeUIForMediaStream, with the exception  being that this flag does NOT affect screen-capture. | kAutoAcceptCameraAndMicrophoneCapture |  | ../chromium/src/content/public/common/content_switches.cc |
| --crash-test |  Causes the browser process to crash on startup. | kBrowserCrashTest |  | ../chromium/src/content/public/common/content_switches.cc |
| --browser-startup-dialog |  Causes the browser process to display a dialog on launch. | kBrowserStartupDialog |  | ../chromium/src/content/public/common/content_switches.cc |
| --browser-subprocess-path |  Path to the exe to run for the renderer and plugin subprocesses. | kBrowserSubprocessPath |  | ../chromium/src/content/public/common/content_switches.cc |
| --browser-test |  Tells whether the code is running browser tests (this changes the startup URL  used by the content shell and also disables features that can make tests  flaky [like monitoring of memory pressure]). | kBrowserTest |  | ../chromium/src/content/public/common/content_switches.cc |
| --change-stack-guard-on-fork |  After a zygote forks a new process, change the stack canary. This switch is  useful so not all forked processes use the same canary (a secret value),  which can be vulnerable to information leaks and brute force attacks. See  https:crbug.com/1206626.  This requires that all functions on the stack at the time  content::RunZygote() is called be compiled without stack canaries.  Valid values are "enable" or "disable". | kChangeStackGuardOnFork |  | ../chromium/src/content/public/common/content_switches.cc |
| --enable |  | kChangeStackGuardOnForkEnabled |  | ../chromium/src/content/public/common/content_switches.cc |
| --disable |  | kChangeStackGuardOnForkDisabled |  | ../chromium/src/content/public/common/content_switches.cc |
| --disable-canvas-aa |  Disable antialiasing on 2d canvas. | kDisable2dCanvasAntialiasing |  | ../chromium/src/content/public/common/content_switches.cc |
| --disable-2d-canvas-image-chromium |  Disables Canvas2D rendering into a scanout buffer for overlay support. | kDisable2dCanvasImageChromium |  | ../chromium/src/content/public/common/content_switches.cc |
| --disable-3d-apis |  Disables client-visible 3D APIs, in particular WebGL and Pepper 3D.  This is controlled by policy and is kept separate from the other  enable/disable switches to avoid accidentally regressing the policy  support for controlling access to these APIs. | kDisable3DAPIs |  | ../chromium/src/content/public/common/content_switches.cc |
| --disable-accelerated-2d-canvas |  Disable gpu-accelerated 2d canvas. | kDisableAccelerated2dCanvas |  | ../chromium/src/content/public/common/content_switches.cc |
| --canvas-2d-layers |  Enable in-progress canvas 2d API methods BeginLayer and EndLayer. | kEnableCanvas2DLayers |  | ../chromium/src/content/public/common/content_switches.cc |
| --disable-accelerated-video-decode |  Disables hardware acceleration of video decode, where available.  Warning: do not remove or rename this flag, as it is used inside ChromeOS  code to implement the DeviceHardwareVideoDecodingEnabled policy. | kDisableAcceleratedVideoDecode |  | ../chromium/src/content/public/common/content_switches.cc |
| --disable-accelerated-video-encode |  Disables hardware acceleration of video encode, where available. | kDisableAcceleratedVideoEncode |  | ../chromium/src/content/public/common/content_switches.cc |
| --disable-backing-store-limit |  Disable limits on the number of backing stores. Can prevent blinking for  users with many windows/tabs and lots of memory. | kDisableBackingStoreLimit |  | ../chromium/src/content/public/common/content_switches.cc |
| --disable-backgrounding-occluded-windows |  Disable backgrounding renders for occluded windows. Done for tests to avoid  nondeterministic behavior. | kDisableBackgroundingOccludedWindowsForTesting |  | ../chromium/src/content/public/common/content_switches.cc |
| --disable-background-timer-throttling |  Disable task throttling of timer tasks from background pages. | kDisableBackgroundTimerThrottling |  | ../chromium/src/content/public/common/content_switches.cc |
| --disable-back-forward-cache |  Disables the BackForwardCache feature. | kDisableBackForwardCache |  | ../chromium/src/content/public/common/content_switches.cc |
| --disable-blink-features |  Disable one or more Blink runtime-enabled features.  Use names from runtime_enabled_features.json5, separated by commas.  Applied after kEnableBlinkFeatures, and after other flags that change these  features. | kDisableBlinkFeatures |  | ../chromium/src/content/public/common/content_switches.cc |
| --disable-databases |  Disables HTML5 DB support. | kDisableDatabases |  | ../chromium/src/content/public/common/content_switches.cc |
| --disable-domain-blocking-for-3d-apis |  Disable the per-domain blocking for 3D APIs after GPU reset.  This switch is intended only for tests. | kDisableDomainBlockingFor3DAPIs |  | ../chromium/src/content/public/common/content_switches.cc |
| --disable-in-process-stack-traces |  Disables the in-process stack traces. | kDisableInProcessStackTraces |  | ../chromium/src/content/public/common/content_switches.cc |
| --disable-webgl |  Disable all versions of WebGL. | kDisableWebGL |  | ../chromium/src/content/public/common/content_switches.cc |
| --disable-webgl2 |  Disable WebGL2. | kDisableWebGL2 |  | ../chromium/src/content/public/common/content_switches.cc |
| --disable-file-system |  Disable FileSystem API. | kDisableFileSystem |  | ../chromium/src/content/public/common/content_switches.cc |
| --disable-gesture-requirement-for-presentation |  Disable user gesture requirement for presentation. | kDisableGestureRequirementForPresentation |  | ../chromium/src/content/public/common/content_switches.cc |
| --disable-gpu |  Disables GPU hardware acceleration.  If software renderer is not in place,  then the GPU process won't launch. | kDisableGpu |  | ../chromium/src/content/public/common/content_switches.cc |
| --disable-gpu-compositing |  Prevent the compositor from using its GPU implementation. | kDisableGpuCompositing |  | ../chromium/src/content/public/common/content_switches.cc |
| --disable-gpu-early-init |  Disable proactive early init of GPU process. | kDisableGpuEarlyInit |  | ../chromium/src/content/public/common/content_switches.cc |
| --disable-gpu-memory-buffer-compositor-resources |  Do not force that all compositor resources be backed by GPU memory buffers. | kDisableGpuMemoryBufferCompositorResources |  | ../chromium/src/content/public/common/content_switches.cc |
| --disable-gpu-memory-buffer-video-frames |  Disable GpuMemoryBuffer backed VideoFrames. | kDisableGpuMemoryBufferVideoFrames |  | ../chromium/src/content/public/common/content_switches.cc |
| --disable-gpu-process-crash-limit |  For tests, to disable the limit on the number of times the GPU process may be  restarted. | kDisableGpuProcessCrashLimit |  | ../chromium/src/content/public/common/content_switches.cc |
| --disable-software-compositing-fallback |  For tests, to disable falling back to software compositing if the GPU Process  has crashed, and reached the GPU Process crash limit. | kDisableSoftwareCompositingFallback |  | ../chromium/src/content/public/common/content_switches.cc |
| --disable-gpu-watchdog |  Disable the thread that crashes the GPU process if it stops responding to  messages. | kDisableGpuWatchdog |  | ../chromium/src/content/public/common/content_switches.cc |
| --disable-ipc-flooding-protection |  Disables the IPC flooding protection.  It is activated by default. Some javascript functions can be used to flood  the browser process with IPC. This protection limits the rate at which they  can be used. | kDisableIpcFloodingProtection |  | ../chromium/src/content/public/common/content_switches.cc |
| --disable-hang-monitor |  Suppresses hang monitor dialogs in renderer processes.  This may allow slow  unload handlers on a page to prevent the tab from closing, but the Task  Manager can be used to terminate the offending process in this case. | kDisableHangMonitor |  | ../chromium/src/content/public/common/content_switches.cc |
| --disable-histogram-customizer |  Disable the RenderThread's HistogramCustomizer. | kDisableHistogramCustomizer |  | ../chromium/src/content/public/common/content_switches.cc |
| --disable-kill-after-bad-ipc |  Don't kill a child process when it sends a bad IPC message.  Apart  from testing, it is a bad idea from a security perspective to enable  this switch. | kDisableKillAfterBadIPC |  | ../chromium/src/content/public/common/content_switches.cc |
| --disable-lcd-text |  Disables LCD text. | kDisableLCDText |  | ../chromium/src/content/public/common/content_switches.cc |
| --disable-local-storage |  Disable LocalStorage. | kDisableLocalStorage |  | ../chromium/src/content/public/common/content_switches.cc |
| --disable-logging |  Force logging to be disabled.  Logging is enabled by default in debug  builds. | kDisableLogging |  | ../chromium/src/content/public/common/content_switches.cc |
| --disable-low-latency-dxva |  Disables using CODECAPI_AVLowLatencyMode when creating DXVA decoders. | kDisableLowLatencyDxva |  | ../chromium/src/content/public/common/content_switches.cc |
| --disable-mojo-broker |  Disables Mojo broker capabilities in the browser during Mojo initialization. | kDisableMojoBroker |  | ../chromium/src/content/public/common/content_switches.cc |
| --disable-new-content-rendering-timeout |  Disables clearing the rendering output of a renderer when it didn't commit  new output for a while after a top-frame navigation. | kDisableNewContentRenderingTimeout |  | ../chromium/src/content/public/common/content_switches.cc |
| --disable-notifications |  Disables the Web Notification and the Push APIs. | kDisableNotifications |  | ../chromium/src/content/public/common/content_switches.cc |
| --disable-pepper-3d |  Disable Pepper3D. | kDisablePepper3d |  | ../chromium/src/content/public/common/content_switches.cc |
| --disable-pinch |  Disables compositor-accelerated touch-screen pinch gestures. | kDisablePinch |  | ../chromium/src/content/public/common/content_switches.cc |
| --disable-presentation-api |  Disables the Presentation API. | kDisablePresentationAPI |  | ../chromium/src/content/public/common/content_switches.cc |
| --disable-pushstate-throttle |  Disables throttling of history.pushState/replaceState calls. | kDisablePushStateThrottle |  | ../chromium/src/content/public/common/content_switches.cc |
| --disable-reading-from-canvas |  Taints all <canvas> elements, regardless of origin. | kDisableReadingFromCanvas |  | ../chromium/src/content/public/common/content_switches.cc |
| --disable-remote-fonts |  Disables remote web font support. SVG font should always work whether this  option is specified or not. | kDisableRemoteFonts |  | ../chromium/src/content/public/common/content_switches.cc |
| --disable-remote-playback-api |  Disables the RemotePlayback API. | kDisableRemotePlaybackAPI |  | ../chromium/src/content/public/common/content_switches.cc |
| --disable-renderer-backgrounding |  Prevent renderer process backgrounding when set. | kDisableRendererBackgrounding |  | ../chromium/src/content/public/common/content_switches.cc |
| --disable-resource-scheduler |  Whether the ResourceScheduler is disabled.  Note this is only useful for C++  Headless embedders who need to implement their own resource scheduling. | kDisableResourceScheduler |  | ../chromium/src/content/public/common/content_switches.cc |
| --disable-shared-workers |  Disable shared workers. | kDisableSharedWorkers |  | ../chromium/src/content/public/common/content_switches.cc |
| --disable-skia-runtime-opts |  Do not use runtime-detected high-end CPU optimizations in Skia.  This is  useful for forcing a baseline code path for e.g. web tests. | kDisableSkiaRuntimeOpts |  | ../chromium/src/content/public/common/content_switches.cc |
| --disable-smooth-scrolling |  Disable smooth scrolling for testing. | kDisableSmoothScrolling |  | ../chromium/src/content/public/common/content_switches.cc |
| --disable-software-rasterizer |  Disables the use of a 3D software rasterizer. | kDisableSoftwareRasterizer |  | ../chromium/src/content/public/common/content_switches.cc |
| --disable-speech-api |  Disables the Web Speech API (both speech recognition and synthesis). | kDisableSpeechAPI |  | ../chromium/src/content/public/common/content_switches.cc |
| --disable-speech-synthesis-api |  Disables the speech synthesis part of Web Speech API. | kDisableSpeechSynthesisAPI |  | ../chromium/src/content/public/common/content_switches.cc |
| --disable-threaded-compositing |  Disable multithreaded GPU compositing of web content. | kDisableThreadedCompositing |  | ../chromium/src/content/public/common/content_switches.cc |
| --disable-v8-idle-tasks |  Disable V8 idle tasks. | kDisableV8IdleTasks |  | ../chromium/src/content/public/common/content_switches.cc |
| --disable-webgl-image-chromium |  Disables WebGL rendering into a scanout buffer for overlay support. | kDisableWebGLImageChromium |  | ../chromium/src/content/public/common/content_switches.cc |
| --disable-web-security |  Don't enforce the same-origin policy; meant for website testing only.  This switch has no effect unless --user-data-dir (as defined by the content  embedder) is also present. | kDisableWebSecurity |  | ../chromium/src/content/public/common/content_switches.cc |
| --disable-zero-copy-dxgi-video |  Disable the video decoder from drawing directly to a texture. | kDisableZeroCopyDxgiVideo |  | ../chromium/src/content/public/common/content_switches.cc |
| --dom-automation |  Specifies if the |DOMAutomationController| needs to be bound in the  renderer. This binding happens on per-frame basis and hence can potentially  be a performance bottleneck. One should only enable it when automating dom  based tests. | kDomAutomationController |  | ../chromium/src/content/public/common/content_switches.cc |
| --disable-2d-canvas-clip-aa |  Disable antialiasing on 2d canvas clips | kDisable2dCanvasClipAntialiasing |  | ../chromium/src/content/public/common/content_switches.cc |
| --disable-yuv-image-decoding |  Disable YUV image decoding for those formats and cases where it's supported.  Has no effect unless GPU rasterization is enabled. | kDisableYUVImageDecoding |  | ../chromium/src/content/public/common/content_switches.cc |
| --enable-lcd-text |  Enables LCD text. | kEnableLCDText |  | ../chromium/src/content/public/common/content_switches.cc |
| --enable-blink-features |  Enable one or more Blink runtime-enabled features.  Use names from runtime_enabled_features.json5, separated by commas.  Applied before kDisableBlinkFeatures, and after other flags that change these  features. | kEnableBlinkFeatures |  | ../chromium/src/content/public/common/content_switches.cc |
| --enable-caret-browsing |  Enable native caret browsing, in which a moveable cursor is placed on a web  page, allowing a user to select and navigate through non-editable text using  just a keyboard. See https:crbug.com/977390 for links to i2i. | kEnableCaretBrowsing |  | ../chromium/src/content/public/common/content_switches.cc |
| --enable-experimental-cookie-features |  Flag that turns on a group of experimental/newly added cookie-related  features together, as a convenience for e.g. testing, to avoid having to set  multiple switches individually which may be error-prone (not to mention  tedious). There is not a corresponding switch to disable all these features,  because that is discouraged, and for testing purposes you'd need to switch  them off individually to identify the problematic feature anyway.   At present this turns on:    net::features::kSameSiteDefaultChecksMethodRigorously    net::features::kCookieSameSiteConsidersRedirectChain    net::features::kEnablePortBoundCookies    net::features::kEnableSchemeBoundCookies | kEnableExperimentalCookieFeatures |  | ../chromium/src/content/public/common/content_switches.cc |
| --enable-experimental-webassembly-features |  Enables experimental WebAssembly features. | kEnableExperimentalWebAssemblyFeatures |  | ../chromium/src/content/public/common/content_switches.cc |
| --enable-experimental-web-platform-features |  Enables Web Platform features that are in development. | kEnableExperimentalWebPlatformFeatures |  | ../chromium/src/content/public/common/content_switches.cc |
| --enable-blink-test-features |  Enables blink runtime enabled features with status:"test" or  status:"experimental", which are enabled when running web tests. | kEnableBlinkTestFeatures |  | ../chromium/src/content/public/common/content_switches.cc |
| --disable-origin-trial-controlled-blink-features |  Disables all RuntimeEnabledFeatures that can be enabled via OriginTrials. | kDisableOriginTrialControlledBlinkFeatures |  | ../chromium/src/content/public/common/content_switches.cc |
| --enable-gpu-memory-buffer-video-frames |  Enable GpuMemoryBuffer backed VideoFrames. | kEnableGpuMemoryBufferVideoFrames |  | ../chromium/src/content/public/common/content_switches.cc |
| --enable-isolated-web-apps-in-renderer |  Enables Isolated Web Apps (IWAs) in a renderer process. There are two ways  to enable the IWAs: by feature flag and by enterprise policy. If IWAs are  enabled by any of the mentioned above ways then this flag is passed to  the renderer process. This flag should not be used from command line.  To enable IWAs from command line one should use kIsolatedWebApps feature  flag. | kEnableIsolatedWebAppsInRenderer |  | ../chromium/src/content/public/common/content_switches.cc |
| --enable-logging |  Force logging to be enabled.  Logging is disabled by default in release  builds. | kEnableLogging |  | ../chromium/src/content/public/common/content_switches.cc |
| --enable-network-information-downlink-max |  Enables the type, downlinkMax attributes of the NetInfo API. Also, enables  triggering of change attribute of the NetInfo API when there is a change in  the connection type. | kEnableNetworkInformationDownlinkMax |  | ../chromium/src/content/public/common/content_switches.cc |
| --disable-nv12-dxgi-video |  Disables the video decoder from drawing to an NV12 textures instead of ARGB. | kDisableNv12DxgiVideo |  | ../chromium/src/content/public/common/content_switches.cc |
| --enable-plugin-placeholder-testing |  Enables testing features of the Plugin Placeholder. For internal use only. | kEnablePluginPlaceholderTesting |  | ../chromium/src/content/public/common/content_switches.cc |
| --enable-precise-memory-info |  Make the values returned to window.performance.memory more granular and more  up to date in shared worker. Without this flag, the memory information is  still available, but it is bucketized and updated less frequently. This flag  also applys to workers. | kEnablePreciseMemoryInfo |  | ../chromium/src/content/public/common/content_switches.cc |
| --enable-privacy-sandbox-ads-apis |  Enables Privacy Sandbox APIs: Attribution Reporting, Fledge, Topics, Fenced  Frames, Shared Storage, Private Aggregation, and their associated features. | kEnablePrivacySandboxAdsApis |  | ../chromium/src/content/public/common/content_switches.cc |
| --v8-cache-options |  Set options to cache V8 data. (none, code, or default) | kV8CacheOptions |  | ../chromium/src/content/public/common/content_switches.cc |
| --enable-service-binary-launcher |  If true the ServiceProcessLauncher is used to launch services. This allows  for service binaries to be loaded rather than using the utility process. This  is only useful for tests. | kEnableServiceBinaryLauncher |  | ../chromium/src/content/public/common/content_switches.cc |
| --enable-skia-benchmarking |  Enables the Skia benchmarking extension. | kEnableSkiaBenchmarking |  | ../chromium/src/content/public/common/content_switches.cc |
| --enable-smooth-scrolling |  On platforms that support it, enables smooth scroll animation. | kEnableSmoothScrolling |  | ../chromium/src/content/public/common/content_switches.cc |
| --enable-spatial-navigation |  Enable spatial navigation | kEnableSpatialNavigation |  | ../chromium/src/content/public/common/content_switches.cc |
| --enable-strict-mixed-content-checking |  Blocks all insecure requests from secure contexts, and prevents the user  from overriding that decision. | kEnableStrictMixedContentChecking |  | ../chromium/src/content/public/common/content_switches.cc |
| --enable-strict-powerful-feature-restrictions |  Blocks insecure usage of a number of powerful features (device orientation,  for example) that we haven't yet deprecated for the web at large. | kEnableStrictPowerfulFeatureRestrictions |  | ../chromium/src/content/public/common/content_switches.cc |
| --enable-tracing-fraction |  When specified along with a value in the range (0,1] will --enable-tracing  for (roughly) that percentage of tests being run. This is done in a stable  manner such that the same tests are chosen each run, and under the assumption  that tests hash equally across the range of possible values.  The flag will enable all tracing categories for those tests, and none for the  rest. This flag could be used with other tracing switches like  --enable-tracing-format, but any other switches that will enable tracing will  turn tracing on for all tests. | kEnableTracingFraction |  | ../chromium/src/content/public/common/content_switches.cc |
| --enable-usermedia-screen-capturing |  Enable screen capturing support for MediaStream API. | kEnableUserMediaScreenCapturing |  | ../chromium/src/content/public/common/content_switches.cc |
| --enable-viewport |  Enables the use of the @viewport CSS rule, which allows  pages to control aspects of their own layout. This also turns on touch-screen  pinch gestures. | kEnableViewport |  | ../chromium/src/content/public/common/content_switches.cc |
| --enable-vtune-support |  Enable the Vtune profiler support. | kEnableVtune |  | ../chromium/src/content/public/common/content_switches.cc |
| --enable-web-auth-deprecated-mojo-testing-api |  Enable the WebAuthn Mojo Testing API. This is a way to interact with the  virtual authenticator environment through a mojo interface and is supported  only to run web-platform-tests on content shell.  Removal of this deprecated API is blocked on crbug.com/937369. | kEnableWebAuthDeprecatedMojoTestingApi |  | ../chromium/src/content/public/common/content_switches.cc |
| --enable-webgl-developer-extensions |  Enables WebGL developer extensions which are not generally exposed  to the web platform. | kEnableWebGLDeveloperExtensions |  | ../chromium/src/content/public/common/content_switches.cc |
| --enable-webgl-draft-extensions |  Enables WebGL extensions not yet approved by the community. | kEnableWebGLDraftExtensions |  | ../chromium/src/content/public/common/content_switches.cc |
| --enable-webgl-image-chromium |  Enables WebGL rendering into a scanout buffer for overlay support. | kEnableWebGLImageChromium |  | ../chromium/src/content/public/common/content_switches.cc |
| --file-url-path-alias |  Define an alias root directory which is replaced with the replacement string  in file URLs. The format is "/alias=/replacement", which would turn  file:/alias/some/path.html into file:/replacement/some/path.html. | kFileUrlPathAlias |  | ../chromium/src/content/public/common/content_switches.cc |
| --force-presentation-receiver-for-testing |  This forces pages to be loaded as presentation receivers.  Useful for testing  behavior specific to presentation receivers.  Spec: https:www.w3.org/TR/presentation-api/#interface-presentationreceiver | kForcePresentationReceiverForTesting |  | ../chromium/src/content/public/common/content_switches.cc |
| --gpu-launcher |  Extra command line options for launching the GPU process (normally used  for debugging). Use like renderer-cmd-prefix. | kGpuLauncher |  | ../chromium/src/content/public/common/content_switches.cc |
| --gpu-process |  Makes this process a GPU sub-process. | kGpuProcess |  | ../chromium/src/content/public/common/content_switches.cc |
| --gpu-sandbox-start-early |  Starts the GPU sandbox before creating a GL context. | kGpuSandboxStartEarly |  | ../chromium/src/content/public/common/content_switches.cc |
| --gpu-startup-dialog |  Causes the GPU process to display a dialog on launch. | kGpuStartupDialog |  | ../chromium/src/content/public/common/content_switches.cc |
| --hide-scrollbars |  Prevents creating scrollbars for web content. Useful for taking consistent  screenshots. | kHideScrollbars |  | ../chromium/src/content/public/common/content_switches.cc |
| --in-process-gpu |  Run the GPU process as a thread in the browser process. | kInProcessGPU |  | ../chromium/src/content/public/common/content_switches.cc |
| --ipc-connection-timeout |  Overrides the timeout, in seconds, that a child process waits for a  connection from the browser before killing itself. | kIPCConnectionTimeout |  | ../chromium/src/content/public/common/content_switches.cc |
| --isolate-origins |  Require dedicated processes for a set of origins, specified as a  comma-separated list. For example:    --isolate-origins=https:www.foo.com,https:www.bar.com | kIsolateOrigins |  | ../chromium/src/content/public/common/content_switches.cc |
| --isolation-by-default |  Enables the web-facing behaviors that will enable origin-isolation by default  at some point in the relatively near future.   https:crbug.com/1140371 | kIsolationByDefault |  | ../chromium/src/content/public/common/content_switches.cc |
| --disable-javascript-harmony-shipping |  Disable latest shipping ECMAScript 6 features. | kDisableJavaScriptHarmonyShipping |  | ../chromium/src/content/public/common/content_switches.cc |
| --javascript-harmony |  Enables experimental Harmony (ECMAScript 6) features. | kJavaScriptHarmony |  | ../chromium/src/content/public/common/content_switches.cc |
| --as-browser |  Flag to launch tests in the browser process. | kLaunchAsBrowser |  | ../chromium/src/content/public/common/content_switches.cc |
| --log-gpu-control-list-decisions |  Logs GPU control list decisions when enforcing blocklist rules. | kLogGpuControlListDecisions |  | ../chromium/src/content/public/common/content_switches.cc |
| --log-level |  Sets the minimum log level. Valid values are from 0 to 3:  INFO = 0, WARNING = 1, LOG_ERROR = 2, LOG_FATAL = 3. | kLoggingLevel |  | ../chromium/src/content/public/common/content_switches.cc |
| --log-file |  Overrides the default file name to use for general-purpose logging (does not  affect which events are logged). | kLogFile |  | ../chromium/src/content/public/common/content_switches.cc |
| --log-missing-unload-ack |  Log an error whenever the unload timeout for a render frame is exceeded. | kLogMissingUnloadACK |  | ../chromium/src/content/public/common/content_switches.cc |
| --max-active-webgl-contexts |  Allows user to override maximum number of active WebGL contexts per  renderer process. | kMaxActiveWebGLContexts |  | ../chromium/src/content/public/common/content_switches.cc |
| --max-decoded-image-size-mb |  Sets the maximium decoded image size limitation. | kMaxDecodedImageSizeMb |  | ../chromium/src/content/public/common/content_switches.cc |
| --max-web-media-player-count |  Sets the maximum number of WebMediaPlayers allowed per frame. | kMaxWebMediaPlayerCount |  | ../chromium/src/content/public/common/content_switches.cc |
| --message-loop-type-ui |  Indicates the utility process should run with a message loop type of UI. | kMessageLoopTypeUi |  | ../chromium/src/content/public/common/content_switches.cc |
| --mock-cert-verifier-default-result-for-testing |  Set the default result for MockCertVerifier. This only works in test code. | kMockCertVerifierDefaultResultForTesting |  | ../chromium/src/content/public/common/content_switches.cc |
| --mojo-local-storage |  Use a Mojo-based LocalStorage implementation. | kMojoLocalStorage |  | ../chromium/src/content/public/common/content_switches.cc |
| --no-unsandboxed-zygote |  Disables the unsandboxed zygote.  Note: this flag should not be used on most platforms. It is introduced  because some platforms (e.g. Cast) have very limited memory and binaries  won't be updated when the browser process is running. | kNoUnsandboxedZygote |  | ../chromium/src/content/public/common/content_switches.cc |
| --no-zygote |  Disables the use of a zygote process for forking child processes. Instead,  child processes will be forked and exec'd directly. Note that --no-sandbox  should also be used together with this flag because the sandbox needs the  zygote to work. | kNoZygote |  | ../chromium/src/content/public/common/content_switches.cc |
| --override-language-detection |  Overrides the language detection result determined based on the page  contents. | kOverrideLanguageDetection |  | ../chromium/src/content/public/common/content_switches.cc |
| --pdf-renderer |  Renderer process that runs the non-PPAPI PDF plugin. | kPdfRenderer |  | ../chromium/src/content/public/common/content_switches.cc |
| --ppapi-in-process |  Runs PPAPI (Pepper) plugins in-process. | kPpapiInProcess |  | ../chromium/src/content/public/common/content_switches.cc |
| --ppapi-plugin-launcher |  Specifies a command that should be used to launch the ppapi plugin process.  Useful for running the plugin process through purify or quantify.  Ex:    --ppapi-plugin-launcher="path\to\purify /Run=yes" | kPpapiPluginLauncher |  | ../chromium/src/content/public/common/content_switches.cc |
| --ppapi |  Argument to the process type that indicates a PPAPI plugin process type. | kPpapiPluginProcess |  | ../chromium/src/content/public/common/content_switches.cc |
| --ppapi-startup-dialog |  Causes the PPAPI sub process to display a dialog on launch. Be sure to use  --no-sandbox as well or the sandbox won't allow the dialog to display. | kPpapiStartupDialog |  | ../chromium/src/content/public/common/content_switches.cc |
| --private-aggregation-developer-mode |  Causes the Private Aggregation API to run without reporting delays. | kPrivateAggregationDeveloperMode |  | ../chromium/src/content/public/common/content_switches.cc |
| --process-per-site |  Enable the "Process Per Site" process model for all domains. This mode  consolidates same-site pages so that they share a single process.   More details here:  - https:www.chromium.org/developers/design-documents/process-models  - The class comment in site_instance.h, listing the supported process models.   IMPORTANT: This isn't to be confused with --site-per-process (which is about  isolation, not consolidation). You probably want the other one. | kProcessPerSite |  | ../chromium/src/content/public/common/content_switches.cc |
| --process-per-tab |  Runs each set of script-connected tabs (i.e., a BrowsingInstance) in its own  renderer process.  We default to using a renderer process for each  site instance (i.e., group of pages from the same registered domain with  script connections to each other).  TODO(creis): This flag is currently a no-op.  We should refactor it to avoid  "unnecessary" process swaps for cross-site navigations but still swap when  needed for security (e.g., isolated origins). | kProcessPerTab |  | ../chromium/src/content/public/common/content_switches.cc |
| --type |  The value of this switch determines whether the process is started as a  renderer or plugin host.  If it's empty, it's the browser. | kProcessType |  | ../chromium/src/content/public/common/content_switches.cc |
| --protected-audiences-consented-debug-token |  Causes Protected Audiences Bidding and Auction API to supply the provided  debugging key to the trusted auction server. This tells the server that it  okay to log information about this user's auction to help with debugging. | kProtectedAudiencesConsentedDebugToken |  | ../chromium/src/content/public/common/content_switches.cc |
| --pull-to-refresh |  Enables or disables pull-to-refresh gesture in response to vertical  overscroll.  Set the value to '0' to disable the feature, set to '1' to enable it for both  touchpad and touchscreen, and set to '2' to enable it only for touchscreen.  Defaults to disabled. | kPullToRefresh |  | ../chromium/src/content/public/common/content_switches.cc |
| --quota-change-event-interval |  Specifies the minimum amount of time, in seconds, that must pass before  consecutive quota change events can be fired. Set the value to '0' to disable  the debounce mechanimsm. | kQuotaChangeEventInterval |  | ../chromium/src/content/public/common/content_switches.cc |
| --reduce-accept-language |  Reduce the accept-language http header, and only send one language in the  request header: https:github.com/Tanych/accept-language. | kReduceAcceptLanguage |  | ../chromium/src/content/public/common/content_switches.cc |
| --reduce-user-agent-minor-version |  Reduce the minor version number in the User-Agent string. This flag  implements phase 4 of User-Agent reduction:  https:blog.chromium.org/2021/09/user-agent-reduction-origin-trial-and-dates.html. | kReduceUserAgentMinorVersion |  | ../chromium/src/content/public/common/content_switches.cc |
| --reduce-user-agent-platform-oscpu |  Reduce the platform and oscpu in the desktop User-Agent string. This flag  implements phase 5 of User-Agent reduction:  https:blog.chromium.org/2021/09/user-agent-reduction-origin-trial-and-dates.html. | kReduceUserAgentPlatformOsCpu |  | ../chromium/src/content/public/common/content_switches.cc |
| --register-pepper-plugins |  Register Pepper plugins (see pepper_plugin_list.cc for its format). | kRegisterPepperPlugins |  | ../chromium/src/content/public/common/content_switches.cc |
| --remote-debugging-pipe |  Enables remote debug over stdio pipes [in=3, out=4] or over the remote pipes  specified in the 'remote-debugging-io-pipes' switch.  Optionally, specifies the format for the protocol messages, can be either  "JSON" (the default) or "CBOR". | kRemoteDebuggingPipe |  | ../chromium/src/content/public/common/content_switches.cc |
| --remote-debugging-port |  Enables remote debug over HTTP on the specified port. | kRemoteDebuggingPort |  | ../chromium/src/content/public/common/content_switches.cc |
| --remote-allow-origins |  Enables web socket connections from the specified origins only. '*' allows  any origin. | kRemoteAllowOrigins |  | ../chromium/src/content/public/common/content_switches.cc |
| --renderer-client-id |  | kRendererClientId |  | ../chromium/src/content/public/common/content_switches.cc |
| --renderer-cmd-prefix |  The contents of this flag are prepended to the renderer command line.  Useful values might be "valgrind" or "xterm -e gdb --args". | kRendererCmdPrefix |  | ../chromium/src/content/public/common/content_switches.cc |
| --renderer |  Causes the process to run as renderer instead of as browser. | kRendererProcess |  | ../chromium/src/content/public/common/content_switches.cc |
| --launch-time-ticks |  Time the browser launched the renderer process (in TimeTicks). | kRendererProcessLaunchTimeTicks |  | ../chromium/src/content/public/common/content_switches.cc |
| --renderer-process-limit |  Overrides the default/calculated limit to the number of renderer processes.  Very high values for this setting can lead to high memory/resource usage  or instability. | kRendererProcessLimit |  | ../chromium/src/content/public/common/content_switches.cc |
| --renderer-startup-dialog |  Causes the renderer process to display a dialog on launch. Passing this flag  also adds sandbox::policy::kNoSandbox on Windows non-official builds, since  that's needed to show a dialog. | kRendererStartupDialog |  | ../chromium/src/content/public/common/content_switches.cc |
| --run-manual |  Manual tests only run when --run-manual is specified. This allows writing  tests that don't run automatically but are still in the same test binary.  This is useful so that a team that wants to run a few tests doesn't have to  add a new binary that must be compiled on all builds. | kRunManualTestsFlag |  | ../chromium/src/content/public/common/content_switches.cc |
| --sandbox-ipc |  Causes the process to run as a sandbox IPC subprocess. | kSandboxIPCProcess |  | ../chromium/src/content/public/common/content_switches.cc |
| --shared-files |  Describes the file descriptors passed to a child process in the following  list format:       <file_id>:<descriptor_id>,<file_id>:<descriptor_id>,...   where <file_id> is an ID string from the manifest of the service being  launched and <descriptor_id> is the numeric identifier of the descriptor for  the child process can use to retrieve the file descriptor from the  global descriptor table. | kSharedFiles |  | ../chromium/src/content/public/common/content_switches.cc |
| --single-process |  Runs the renderer and plugins in the same process as the browser | kSingleProcess |  | ../chromium/src/content/public/common/content_switches.cc |
| --site-per-process |  Enforces a one-site-per-process security policy:   * Each renderer process, for its whole lifetime, is dedicated to rendering     pages for just one site.   * Thus, pages from different sites are never in the same process.   * A renderer process's access rights are restricted based on its site.   * All cross-site navigations force process swaps.   * <iframe>s are rendered out-of-process whenever the src= is cross-site.   More details here:  - https:www.chromium.org/developers/design-documents/site-isolation  - https:www.chromium.org/developers/design-documents/process-models  - The class comment in site_instance.h, listing the supported process models.   IMPORTANT: this isn't to be confused with --process-per-site (which is about  process consolidation, not isolation). You probably want this one. | kSitePerProcess |  | ../chromium/src/content/public/common/content_switches.cc |
| --disable-site-isolation-trials |  Disables site isolation.   Note that the opt-in (to site-per-process, isolate-origins, etc.) via  enterprise policy and/or cmdline takes precedence over the  kDisableSiteIsolation switch (i.e. the opt-in takes effect despite potential  presence of kDisableSiteIsolation switch).   Note that for historic reasons the name of the switch misleadingly mentions  "trials", but the switch also disables the default site isolation that ships  on desktop since M67.  The name of the switch is preserved for  backcompatibility of chrome:flags. | kDisableSiteIsolation |  | ../chromium/src/content/public/common/content_switches.cc |
| --start-fullscreen |  Specifies if the browser should start in fullscreen mode, like if the user  had pressed F11 right after startup. | kStartFullscreen |  | ../chromium/src/content/public/common/content_switches.cc |
| --enable-stats-collection-bindings |  Specifies if the |StatsCollectionController| needs to be bound in the  renderer. This binding happens on per-frame basis and hence can potentially  be a performance bottleneck. One should only enable it when running a test  that needs to access the provided statistics. | kStatsCollectionController |  | ../chromium/src/content/public/common/content_switches.cc |
| --skia-font-cache-limit-mb |  Specifies the max number of bytes that should be used by the skia font cache.  If the cache needs to allocate more, skia will purge previous entries. | kSkiaFontCacheLimitMb |  | ../chromium/src/content/public/common/content_switches.cc |
| --skia-resource-cache-limit-mb |  Specifies the max number of bytes that should be used by the skia resource  cache. The previous entries are purged from the cache when the memory useage  exceeds this limit. | kSkiaResourceCacheLimitMb |  | ../chromium/src/content/public/common/content_switches.cc |
| --test-type |  Type of the current test harness ("browser" or "ui" or "gpu"). | kTestType |  | ../chromium/src/content/public/common/content_switches.cc |
| --touch-events |  Enable support for touch event feature detection. | kTouchEventFeatureDetection |  | ../chromium/src/content/public/common/content_switches.cc |
| --auto |  The values the kTouchEventFeatureDetection switch may have, as in  --touch-events=disabled.    auto: enabled at startup when an attached touchscreen is present. | kTouchEventFeatureDetectionAuto |  | ../chromium/src/content/public/common/content_switches.cc |
| --enabled |    enabled: touch events always enabled. | kTouchEventFeatureDetectionEnabled |  | ../chromium/src/content/public/common/content_switches.cc |
| --disabled |    disabled: touch events are disabled. | kTouchEventFeatureDetectionDisabled |  | ../chromium/src/content/public/common/content_switches.cc |
| --time-ticks-at-unix-epoch |  Accepts a number representing the time-ticks value at the Unix epoch.  Since different processes can produce a different value for this due to  system clock changes, this allows synchronizing them to a single value. | kTimeTicksAtUnixEpoch |  | ../chromium/src/content/public/common/content_switches.cc |
| --use-fake-codec-for-peer-connection |  Replaces the existing codecs supported in peer connection with a single fake  codec entry that create a fake video encoder and decoder. | kUseFakeCodecForPeerConnection |  | ../chromium/src/content/public/common/content_switches.cc |
| --use-fake-ui-for-digital-identity |  Bypass the digital-identity-credential OS call. Simulate the user  accepting the OS-presented dialog. | kUseFakeUIForDigitalIdentity |  | ../chromium/src/content/public/common/content_switches.cc |
| --use-fake-ui-for-fedcm |  Bypass the FedCM account selection dialog. If a value is provided for  this switch, that account ID is selected, otherwise the first account  is chosen. | kUseFakeUIForFedCM |  | ../chromium/src/content/public/common/content_switches.cc |
| --use-fake-ui-for-media-stream |  Bypass the media stream infobar by selecting the default device for media  streams (e.g. WebRTC). Works with --use-fake-device-for-media-stream.  Prefer --auto-accept-camera-and-microphone-capture which does not interact  with screen/tab capture. | kUseFakeUIForMediaStream |  | ../chromium/src/content/public/common/content_switches.cc |
| --use-skia-font-manager |  This will replace the existing font manager with SkiaFontManager in the  renderer. | kUseSkiaFontManager | BUILDFLAG(IS_WIN) | ../chromium/src/content/public/common/content_switches.cc |
| --video-image-texture-target |  Texture target for CHROMIUM_image backed video frame textures. | kVideoImageTextureTarget |  | ../chromium/src/content/public/common/content_switches.cc |
| --use-context-snapshot |  Switch supplied to the renderer if the feature `kUseContextSnapshot` is  enabled. A switch is used as at the time the renderer needs this information  features have not yet been loaded. | kUseContextSnapshotSwitch | BUILDFLAG(IS_ANDROID) && BUILDFLAG(INCLUDE_BOTH_V8_SNAPSHOTS) | ../chromium/src/content/public/common/content_switches.cc |
| --use-mobile-user-agent |  Set when Chromium should use a mobile user agent. | kUseMobileUserAgent |  | ../chromium/src/content/public/common/content_switches.cc |
| --use-mock-cert-verifier-for-testing |  Use the MockCertVerifier. This only works in test code. | kUseMockCertVerifierForTesting |  | ../chromium/src/content/public/common/content_switches.cc |
| --utility-cmd-prefix |  The contents of this flag are prepended to the utility process command line.  Useful values might be "valgrind" or "xterm -e gdb --args". | kUtilityCmdPrefix |  | ../chromium/src/content/public/common/content_switches.cc |
| --utility |  Causes the process to run as a utility subprocess. | kUtilityProcess |  | ../chromium/src/content/public/common/content_switches.cc |
| --utility-startup-dialog |  Causes the utility process to display a dialog on launch. | kUtilityStartupDialog |  | ../chromium/src/content/public/common/content_switches.cc |
| --utility-sub-type |  This switch indicates the type of a utility process. It does not affect the  services offered by the process, but is added to the command line for  debugging and profiling purposes. | kUtilitySubType |  | ../chromium/src/content/public/common/content_switches.cc |
| --browser-ui-tests-verify-pixels |  Causes tests to attempt to verify pixel output. | kVerifyPixels |  | ../chromium/src/content/public/common/content_switches.cc |
| --wait-for-debugger-children |  Will add kWaitForDebugger to every child processes. If a value is passed, it  will be used as a filter to determine if the child process should have the  kWaitForDebugger flag passed on or not. | kWaitForDebuggerChildren |  | ../chromium/src/content/public/common/content_switches.cc |
| --wait-for-debugger-on-navigation |  On every navigation a message with the renderer's URL will be logged and the  renderer will wait for a debugger to be attached or SIGUSR1 to be sent to  continue execution. | kWaitForDebuggerOnNavigation |  | ../chromium/src/content/public/common/content_switches.cc |
| --wait-for-debugger-webui |  Flag used by WebUI test runners to wait for debugger to be attached. | kWaitForDebuggerWebUI |  | ../chromium/src/content/public/common/content_switches.cc |
| --webauthn-remote-desktop-support |  Allows trusted remote desktop clients to make WebAuthn requests on behalf of  other origins. This switch only controls availability of the  `remoteDesktopClientOverride` extension but doesn't by itself enable any  origin to use it. | kWebAuthRemoteDesktopSupport |  | ../chromium/src/content/public/common/content_switches.cc |
| --webgl-antialiasing-mode |  Set the antialiasing method used for webgl. (none, explicit, implicit) | kWebglAntialiasingMode |  | ../chromium/src/content/public/common/content_switches.cc |
| --webgl-msaa-sample-count |  Set a default sample count for webgl if msaa is enabled. | kWebglMSAASampleCount |  | ../chromium/src/content/public/common/content_switches.cc |
| --zygote-cmd-prefix |  The prefix used when starting the zygote process. (i.e. 'gdb --args') | kZygoteCmdPrefix |  | ../chromium/src/content/public/common/content_switches.cc |
| --zygote |  Causes the process to run as a zygote. | kZygoteProcess |  | ../chromium/src/content/public/common/content_switches.cc |
| --web-otp-backend |  Enables specified backend for the Web OTP API. | kWebOtpBackend |  | ../chromium/src/content/public/common/content_switches.cc |
| --web-otp-backend-sms-verification |  Enables Sms Verification backend for Web OTP API which requires app hash in  SMS body. | kWebOtpBackendSmsVerification |  | ../chromium/src/content/public/common/content_switches.cc |
| --web-otp-backend-user-consent |  Enables User Consent backend for Web OTP API. | kWebOtpBackendUserConsent |  | ../chromium/src/content/public/common/content_switches.cc |
| --web-otp-backend-auto |  Enables auto backend selection for Web OTP API. | kWebOtpBackendAuto |  | ../chromium/src/content/public/common/content_switches.cc |
| --disable-webrtc-encryption |  Disables encryption of RTP Media for WebRTC. When Chrome embeds Content, it  ignores this switch on its stable and beta channels. | kDisableWebRtcEncryption |  | ../chromium/src/content/public/common/content_switches.cc |
| --enable-webrtc-srtp-encrypted-headers |  Enables negotiation of encrypted header extensions from RFC 6904 for SRTP  in WebRTC.  See https:tools.ietf.org/html/rfc6904 for further information.  TODO(crbug.com/40623740): Remove this. | kEnableWebRtcSrtpEncryptedHeaders |  | ../chromium/src/content/public/common/content_switches.cc |
| --enforce-webrtc-ip-permission-check |  Enforce IP Permission check. TODO(guoweis): Remove this once the feature is  not under finch and becomes the default. | kEnforceWebRtcIPPermissionCheck |  | ../chromium/src/content/public/common/content_switches.cc |
| --force-webrtc-ip-handling-policy |  Override WebRTC IP handling policy to mimic the behavior when WebRTC IP  handling policy is specified in Preferences. | kForceWebRtcIPHandlingPolicy |  | ../chromium/src/content/public/common/content_switches.cc |
| --max-gum-fps |  Override the maximum framerate as can be specified in calls to getUserMedia.  This flag expects a value.  Example: --max-gum-fps=17.5 | kWebRtcMaxCaptureFramerate |  | ../chromium/src/content/public/common/content_switches.cc |
| --webrtc-event-logging |  Enable capture and local storage of WebRTC event logs without visiting  chrome:webrtc-internals. This is useful for automated testing. It accepts  the path to which the local logs would be stored. Disabling is not possible  without restarting the browser and relaunching without this flag. | kWebRtcLocalEventLogging |  | ../chromium/src/content/public/common/content_switches.cc |
| --disable-scroll-to-text-fragment |  This switch disables the ScrollToTextFragment feature. | kDisableScrollToTextFragment |  | ../chromium/src/content/public/common/content_switches.cc |
| --force-webxr-runtime |  Forcibly enable and select the specified runtime for webxr.  Note that this provides an alternative means of enabling a runtime, and will  also functionally disable all other runtimes. | kWebXrForceRuntime |  | ../chromium/src/content/public/common/content_switches.cc |
| --no-xr-runtime |  Tell WebXr to assume that it does not support any runtimes. | kWebXrRuntimeNone |  | ../chromium/src/content/public/common/content_switches.cc |
| --orientation-sensors |  | kWebXrRuntimeOrientationSensors |  | ../chromium/src/content/public/common/content_switches.cc |
| --arcore |  The following are the runtimes that WebXr supports. | kWebXrRuntimeArCore |  | ../chromium/src/content/public/common/content_switches.cc |
| --cardboard |  | kWebXrRuntimeCardboard |  | ../chromium/src/content/public/common/content_switches.cc |
| --openxr |  | kWebXrRuntimeOpenXr |  | ../chromium/src/content/public/common/content_switches.cc |
| --disable-media-session-api |  Disable Media Session API | kDisableMediaSessionAPI | BUILDFLAG(IS_ANDROID) | ../chromium/src/content/public/common/content_switches.cc |
| --disable-screen-orientation-lock |  Disable the locking feature of the screen orientation API. | kDisableScreenOrientationLock | BUILDFLAG(IS_ANDROID) | ../chromium/src/content/public/common/content_switches.cc |
| --disable-site-isolation-for-policy |  Just like kDisableSiteIsolation, but doesn't show the "stability and security  will suffer" butter bar warning. | kDisableSiteIsolationForPolicy | BUILDFLAG(IS_ANDROID) | ../chromium/src/content/public/common/content_switches.cc |
| --disable-timeouts-for-profiling |  Disable timeouts that may cause the browser to die when running slowly. This  is useful if running with profiling (such as debug malloc). | kDisableTimeoutsForProfiling | BUILDFLAG(IS_ANDROID) | ../chromium/src/content/public/common/content_switches.cc |
| --enable-adaptive-selection-handle-orientation |  Enable inverting of selection handles so that they are not clipped by the  viewport boundaries. | kEnableAdaptiveSelectionHandleOrientation | BUILDFLAG(IS_ANDROID) | ../chromium/src/content/public/common/content_switches.cc |
| --enable-longpress-drag-selection |  Enable drag manipulation of longpress-triggered text selections. | kEnableLongpressDragSelection | BUILDFLAG(IS_ANDROID) | ../chromium/src/content/public/common/content_switches.cc |
| --force-online-connection-state-for-indicator |  Prevent the offline indicator from showing. | kForceOnlineConnectionStateForIndicator | BUILDFLAG(IS_ANDROID) | ../chromium/src/content/public/common/content_switches.cc |
| --remote-debugging-socket-name |  Enables remote debug over HTTP on the specified socket name. | kRemoteDebuggingSocketName | BUILDFLAG(IS_ANDROID) | ../chromium/src/content/public/common/content_switches.cc |
| --renderer-wait-for-java-debugger |  Block ChildProcessMain thread of the renderer's ChildProcessService until a  Java debugger is attached. | kRendererWaitForJavaDebugger | BUILDFLAG(IS_ANDROID) | ../chromium/src/content/public/common/content_switches.cc |
| --disable-oopr-debug-crash-dump |  Disables debug crash dumps for OOPR. | kDisableOoprDebugCrashDump | BUILDFLAG(IS_ANDROID) | ../chromium/src/content/public/common/content_switches.cc |
| --enable-aggressive-domstorage-flushing |  Enable the aggressive flushing of DOM Storage to minimize data loss. | kEnableAggressiveDOMStorageFlushing |  | ../chromium/src/content/public/common/content_switches.cc |
| --enable-automation |  Enable indication that browser is controlled by automation. | kEnableAutomation |  | ../chromium/src/content/public/common/content_switches.cc |
| --prevent-resizing-contents-for-testing |  For mobile devices, tests should include a viewport meta tag to specify page  dimension adjustments. Omitting the tag can lead to automatic resizing to  the standard mobile fallback size (980), which results in content shrinking  as it first expands to 980, then scales down to 800 to fit the screen, as  observed in the issue at https:crrev.com/c/4615623.  This flag is intended for use in tests that do not include a viewport meta  tag. When enabled, it ensures the viewport size matches the standard mobile  fallback size, thereby helping to prevent content resizing in such tests. | kPreventResizingContentsForTesting | BUILDFLAG(IS_IOS) | ../chromium/src/content/public/common/content_switches.cc |
| --enable-speech-dispatcher |  Allows sending text-to-speech requests to speech-dispatcher, a common  Linux speech service. Because it's buggy, the user must explicitly  enable it so that visiting a random webpage can't cause instability. | kEnableSpeechDispatcher | BUILDFLAG(IS_LINUX) || BUILDFLAG(IS_CHROMEOS_LACROS) | ../chromium/src/content/public/common/content_switches.cc |
| --llvm-profile-file |  For lacros, we do not use environment variable to pass values. Instead we  use a command line flag to pass the path to the device. | kLLVMProfileFile | BUILDFLAG(IS_LINUX) || BUILDFLAG(IS_CHROMEOS_LACROS) | ../chromium/src/content/public/common/content_switches.cc |
| --device-scale-factor |  Device scale factor passed to certain processes like renderers, etc. | kDeviceScaleFactor | BUILDFLAG(IS_WIN) | ../chromium/src/content/public/common/content_switches.cc |
| --disable-legacy-window |  Disable the Legacy Window which corresponds to the size of the WebContents. | kDisableLegacyIntermediateWindow | BUILDFLAG(IS_WIN) | ../chromium/src/content/public/common/content_switches.cc |
| --font-cache-shared-handle |  DirectWrite FontCache is shared by browser to renderers using shared memory.  This switch allows us to pass the shared memory handle to the renderer. | kFontCacheSharedHandle | BUILDFLAG(IS_WIN) | ../chromium/src/content/public/common/content_switches.cc |
| --ppapi-antialiased-text-enabled |  The boolean value (0/1) of FontRenderParams::antialiasing to be passed to  Ppapi processes. | kPpapiAntialiasedTextEnabled | BUILDFLAG(IS_WIN) | ../chromium/src/content/public/common/content_switches.cc |
| --ppapi-subpixel-rendering-setting |  The enum value of FontRenderParams::subpixel_rendering to be passed to Ppapi  processes. | kPpapiSubpixelRenderingSetting | BUILDFLAG(IS_WIN) | ../chromium/src/content/public/common/content_switches.cc |
| --raise-timer-frequency |  Raise the timer interrupt frequency in all Chrome processes, for experimental  purposes. This feature is needed because as of Windows 10 2004 the scheduling  effects of changing the timer interrupt frequency are not global, and this  lets us prove/disprove whether this matters. See https:crbug.com/1128917 | kRaiseTimerFrequency | BUILDFLAG(IS_WIN) | ../chromium/src/content/public/common/content_switches.cc |
| --gpu2-startup-dialog |  Causes the second GPU process used for gpu info collection to display a  dialog on launch. | kGpu2StartupDialog | BUILDFLAG(IS_WIN) | ../chromium/src/content/public/common/content_switches.cc |
| --audio-process-high-priority |  Use high priority for the audio process. | kAudioProcessHighPriority | BUILDFLAG(IS_WIN) | ../chromium/src/content/public/common/content_switches.cc |
| --remote-debugging-io-pipes |  Specifies pipe names for the incoming and outbound messages on the Windows  platform. This is a comma separated list of two pipe handles serialized as  unsigned integers, e.g. "--remote-debugging-io-pipes=3,4". | kRemoteDebuggingIoPipes | BUILDFLAG(IS_WIN) | ../chromium/src/content/public/common/content_switches.cc |
| switch | description | variable | cpp condition | location |
| ------ | ----------- | -------- | ------------- | -------- |
| --user-data-dir |  Makes Content Shell use the given path for its data directory.  NOTE: "user-data-dir" is used to align with Chromedriver's behavior. Please  do NOT change this to another value.  NOTE: The same value is also used at Java-side in  ContentShellBrowserTestActivity.java#getUserDataDirectoryCommandLineSwitch(). | kContentShellUserDataDir |  | ../chromium/src/content/shell/common/shell_switches.cc |
| --crash-dumps-dir |  The directory breakpad should store minidumps in. | kCrashDumpsDir |  | ../chromium/src/content/shell/common/shell_switches.cc |
| --disable-system-font-check |  Disables the check for the system font when specified. | kDisableSystemFontCheck |  | ../chromium/src/content/shell/common/shell_switches.cc |
| --expose-internals-for-testing |  Exposes the window.internals object to JavaScript for interactive development  and debugging of web tests that rely on it. | kExposeInternalsForTesting |  | ../chromium/src/content/shell/common/shell_switches.cc |
| --content-shell-host-window-size |  Size for the content_shell's host window (i.e. "800x600"). | kContentShellHostWindowSize |  | ../chromium/src/content/shell/common/shell_switches.cc |
| --content-shell-hide-toolbar |  Hides toolbar from content_shell's host window. | kContentShellHideToolbar |  | ../chromium/src/content/shell/common/shell_switches.cc |
| --content-shell-devtools-tab-target |  Let DevTools front-end talk to the target of type "tab" rather than  "frame" when inspecting a WebContents. | kContentShellDevToolsTabTarget | !BUILDFLAG(IS_ANDROID) && !BUILDFLAG(IS_IOS) | ../chromium/src/content/shell/common/shell_switches.cc |
| --isolated-context-origins |  Enables APIs guarded with the [IsolatedContext] IDL attribute for the given  comma-separated list of origins. | kIsolatedContextOrigins |  | ../chromium/src/content/shell/common/shell_switches.cc |
| --remote-debugging-address |  Use the given address instead of the default loopback for accepting remote  debugging connections. Note that the remote debugging protocol does not  perform any authentication, so exposing it too widely can be a security  risk. | kRemoteDebuggingAddress |  | ../chromium/src/content/shell/common/shell_switches.cc |
| --run-web-tests |  Runs Content Shell in web test mode, injecting test-only behaviour for  blink web tests. | kRunWebTests |  | ../chromium/src/content/shell/common/shell_switches.cc |
| --test-register-standard-scheme |  Register the provided scheme as a standard scheme. | kTestRegisterStandardScheme |  | ../chromium/src/content/shell/common/shell_switches.cc |
| switch | description | variable | cpp condition | location |
| ------ | ----------- | -------- | ------------- | -------- |
| --allow-external-pages |  Allow access to external pages during web tests. | kAllowExternalPages |  | ../chromium/src/content/web_test/common/web_test_switches.cc |
| --crash-on-failure |  When specified to "enable-leak-detection" command-line option,  causes the leak detector to cause immediate crash when found leak. | kCrashOnFailure |  | ../chromium/src/content/web_test/common/web_test_switches.cc |
| --debug-devtools |  Run devtools tests in debug mode (not bundled and minified) | kDebugDevTools |  | ../chromium/src/content/web_test/common/web_test_switches.cc |
| --enable-accelerated-2d-canvas |  Enable accelerated 2D canvas. | kEnableAccelerated2DCanvas |  | ../chromium/src/content/web_test/common/web_test_switches.cc |
| --enable-font-antialiasing |  Enable font antialiasing for pixel tests. | kEnableFontAntialiasing |  | ../chromium/src/content/web_test/common/web_test_switches.cc |
| --always-use-complex-text |  Always use the complex text path for web tests. | kAlwaysUseComplexText |  | ../chromium/src/content/web_test/common/web_test_switches.cc |
| --enable-leak-detection |  Enables the leak detection of loading webpages. This allows us to check  whether or not reloading a webpage releases web-related objects correctly. | kEnableLeakDetection |  | ../chromium/src/content/web_test/common/web_test_switches.cc |
| --inspector-protocol-log |  Specifies the path to a file containing a Chrome DevTools protocol log.  Each line in the log file is expected to be a protocol message in the JSON  format. The test runner will use this log file to script the backend for any  inspector-protocol tests that run. Usually you would want to run a single  test using the log to reproduce timeouts or crashes. | kInspectorProtocolLog |  | ../chromium/src/content/web_test/common/web_test_switches.cc |
| --encode-binary |  Encode binary web test results (images, audio) using base64. | kEncodeBinary |  | ../chromium/src/content/web_test/common/web_test_switches.cc |
| --disable-auto-wpt-origin-isolation |  Disables the automatic origin isolation of web platform test domains.  We normally origin-isolate them for better test coverage, but tests of opt-in  origin isolation need to disable this. | kDisableAutoWPTOriginIsolation |  | ../chromium/src/content/web_test/common/web_test_switches.cc |
| --reset-browsing-instance-between-tests |  Forces each web test to be run in a new BrowsingInstance. Required for origin  isolation web tests where the BrowsingInstance retains state from origin  isolation requests, but this flag may benefit other web tests. | kResetBrowsingInstanceBetweenTests |  | ../chromium/src/content/web_test/common/web_test_switches.cc |
| --stable-release-mode |  This makes us disable some web-platform runtime features so that we test  content_shell as if it was a stable release. It is only followed when  kRunWebTest is set. For the features' level, see  third_party/blink/renderer/platform/RuntimeEnabledFeatures.md | kStableReleaseMode |  | ../chromium/src/content/web_test/common/web_test_switches.cc |
| --disable-headless-mode |  Disables the shell from beginning in headless mode. Tests will then attempt  to use the hardware GPU for rendering. This is only followed when  kRunWebTests is set. | kDisableHeadlessMode |  | ../chromium/src/content/web_test/common/web_test_switches.cc |
| switch | description | variable | cpp condition | location |
| ------ | ----------- | -------- | ------------- | -------- |
| --enable-gamepad-button-axis-events |  Enables gamepadbuttondown, gamepadbuttonup, gamepadbuttonchange,  gamepadaxismove non-standard gamepad events. | kEnableGamepadButtonAxisEvents |  | ../chromium/src/device/gamepad/public/cpp/gamepad_switches.cc |
| --restrict-gamepad-access |  Enables Feature Policy and Secure Context requirements on getGamepads. | kRestrictGamepadAccess |  | ../chromium/src/device/gamepad/public/cpp/gamepad_switches.cc |
| --gamepad-polling-interval |  Overrides the gamepad polling interval. Decreasing the interval improves  input latency of buttons and axes but may negatively affect performance due  to more CPU time spent in the input polling thread. | kGamepadPollingInterval |  | ../chromium/src/device/gamepad/public/cpp/gamepad_switches.cc |
| switch | description | variable | cpp condition | location |
| ------ | ----------- | -------- | ------------- | -------- |
| switch | description | variable | cpp condition | location |
| ------ | ----------- | -------- | ------------- | -------- |
| switch | description | variable | cpp condition | location |
| ------ | ----------- | -------- | ------------- | -------- |
| --allow-http-background-page |  | kAllowHTTPBackgroundPage |  | ../chromium/src/extensions/common/switches.cc |
| --allow-legacy-extension-manifests |  | kAllowLegacyExtensionManifests |  | ../chromium/src/extensions/common/switches.cc |
| --allowlisted-extension-id |  | kAllowlistedExtensionID |  | ../chromium/src/extensions/common/switches.cc |
| --embedded-extension-options |  | kEmbeddedExtensionOptions |  | ../chromium/src/extensions/common/switches.cc |
| --enable-ble-advertising-in-apps |  | kEnableBLEAdvertising |  | ../chromium/src/extensions/common/switches.cc |
| --enable-experimental-extension-apis |  | kEnableExperimentalExtensionApis |  | ../chromium/src/extensions/common/switches.cc |
| --disable-extensions-file-access-check |  | kDisableExtensionsFileAccessCheck |  | ../chromium/src/extensions/common/switches.cc |
| --disable-extensions-http-throttling |  | kDisableExtensionsHttpThrottling |  | ../chromium/src/extensions/common/switches.cc |
| --extension-process |  | kExtensionProcess |  | ../chromium/src/extensions/common/switches.cc |
| --extensions-on-chrome-urls |  | kExtensionsOnChromeURLs |  | ../chromium/src/extensions/common/switches.cc |
| --disable-app-content-verification |  | kDisableAppContentVerification |  | ../chromium/src/extensions/common/switches.cc |
| --load-apps |  | kLoadApps |  | ../chromium/src/extensions/common/switches.cc |
| --load-extension |  | kLoadExtension |  | ../chromium/src/extensions/common/switches.cc |
| --load-signin-profile-test-extension |  | kLoadSigninProfileTestExtension | BUILDFLAG(IS_CHROMEOS_ASH) | ../chromium/src/extensions/common/switches.cc |
| --load-guest-mode-test-extension |  | kLoadGuestModeTestExtension | BUILDFLAG(IS_CHROMEOS_ASH) | ../chromium/src/extensions/common/switches.cc |
| --offscreen-document-testing |  | kOffscreenDocumentTesting |  | ../chromium/src/extensions/common/switches.cc |
| --set-extension-throttle-test-params |  | kSetExtensionThrottleTestParams |  | ../chromium/src/extensions/common/switches.cc |
| --show-component-extension-options |  | kShowComponentExtensionOptions |  | ../chromium/src/extensions/common/switches.cc |
| --enable-trace-app-source |  | kTraceAppSource |  | ../chromium/src/extensions/common/switches.cc |
| --enable-crx-hash-check |  | kEnableCrxHashCheck |  | ../chromium/src/extensions/common/switches.cc |
| --allow-future-manifest-version |  | kAllowFutureManifestVersion |  | ../chromium/src/extensions/common/switches.cc |
| --extension-test-api-on-web-pages |  | kExtensionTestApiOnWebPages |  | ../chromium/src/extensions/common/switches.cc |
| switch | description | variable | cpp condition | location |
| ------ | ----------- | -------- | ------------- | -------- |
| --app-shell-allow-roaming |  Allow roaming in the cellular network. | kAppShellAllowRoaming | BUILDFLAG(IS_CHROMEOS_ASH) | ../chromium/src/extensions/shell/common/switches.cc |
| --app-shell-host-window-size |  Size for the host window to create (i.e. "800x600"). | kAppShellHostWindowSize | BUILDFLAG(IS_CHROMEOS_ASH) | ../chromium/src/extensions/shell/common/switches.cc |
| --app-shell-preferred-network |  SSID of the preferred WiFi network. | kAppShellPreferredNetwork | BUILDFLAG(IS_CHROMEOS_ASH) | ../chromium/src/extensions/shell/common/switches.cc |
| switch | description | variable | cpp condition | location |
| ------ | ----------- | -------- | ------------- | -------- |
| switch | description | variable | cpp condition | location |
| ------ | ----------- | -------- | ------------- | -------- |
| --enable-content-directories |  | kEnableContentDirectories |  | ../chromium/src/fuchsia_web/webengine/switches.cc |
| --enable-widevine |  | kEnableWidevine |  | ../chromium/src/fuchsia_web/webengine/switches.cc |
| --incognito |  | kIncognito |  | ../chromium/src/fuchsia_web/webengine/switches.cc |
| --playready-key-system |  | kPlayreadyKeySystem |  | ../chromium/src/fuchsia_web/webengine/switches.cc |
| --remote-debug-mode |  | kEnableRemoteDebugMode |  | ../chromium/src/fuchsia_web/webengine/switches.cc |
| --user-agent-product |  | kUserAgentProductAndVersion |  | ../chromium/src/fuchsia_web/webengine/switches.cc |
| --cors-exempt-headers |  | kCorsExemptHeaders |  | ../chromium/src/fuchsia_web/webengine/switches.cc |
| --enable-cast-streaming-receiver |  | kEnableCastStreamingReceiver |  | ../chromium/src/fuchsia_web/webengine/switches.cc |
| --cdm-data-directory |  | kCdmDataDirectory |  | ../chromium/src/fuchsia_web/webengine/switches.cc |
| --cdm-data-quota-bytes |  | kCdmDataQuotaBytes |  | ../chromium/src/fuchsia_web/webengine/switches.cc |
| --data-quota-bytes |  | kDataQuotaBytes |  | ../chromium/src/fuchsia_web/webengine/switches.cc |
| --google-api-key |  | kGoogleApiKey |  | ../chromium/src/fuchsia_web/webengine/switches.cc |
| --context-provider |  | kContextProvider |  | ../chromium/src/fuchsia_web/webengine/switches.cc |
| --proxy-bypass-list |  | kProxyBypassList |  | ../chromium/src/fuchsia_web/webengine/switches.cc |
| --proxy-server |  | kProxyServer |  | ../chromium/src/fuchsia_web/webengine/switches.cc |
| --allow-running-insecure-content |  | kAllowRunningInsecureContent | BUILDFLAG(ENABLE_CAST_RECEIVER) | ../chromium/src/fuchsia_web/webengine/switches.cc |
| --use-legacy-metrics-service |  | kUseLegacyMetricsService | BUILDFLAG(ENABLE_CAST_RECEIVER) | ../chromium/src/fuchsia_web/webengine/switches.cc |
| switch | description | variable | cpp condition | location |
| ------ | ----------- | -------- | ------------- | -------- |
| --gaia-config |  | kGaiaConfigPath |  | ../chromium/src/google_apis/gaia/gaia_switches.cc |
| --gaia-config-contents |  | kGaiaConfigContents |  | ../chromium/src/google_apis/gaia/gaia_switches.cc |
| --google-url |  | kGoogleUrl |  | ../chromium/src/google_apis/gaia/gaia_switches.cc |
| --gaia-url |  | kGaiaUrl |  | ../chromium/src/google_apis/gaia/gaia_switches.cc |
| --google-apis-url |  | kGoogleApisUrl |  | ../chromium/src/google_apis/gaia/gaia_switches.cc |
| --lso-url |  | kLsoUrl |  | ../chromium/src/google_apis/gaia/gaia_switches.cc |
| --oauth-account-manager-url |  | kOAuthAccountManagerUrl |  | ../chromium/src/google_apis/gaia/gaia_switches.cc |
| --oauth2-client-id |  | kOAuth2ClientID |  | ../chromium/src/google_apis/gaia/gaia_switches.cc |
| --oauth2-client-secret |  | kOAuth2ClientSecret |  | ../chromium/src/google_apis/gaia/gaia_switches.cc |
| switch | description | variable | cpp condition | location |
| ------ | ----------- | -------- | ------------- | -------- |
| --gcm-checkin-url |  Sets the checkin service endpoint that will be used for performing Google  Cloud Messaging checkins. | kGCMCheckinURL |  | ../chromium/src/google_apis/gcm/engine/gservices_switches.cc |
| --gcm-mcs-endpoint |  Sets the Mobile Connection Server endpoint that will be used for Google  Cloud Messaging. | kGCMMCSEndpoint |  | ../chromium/src/google_apis/gcm/engine/gservices_switches.cc |
| --gcm-registration-url |  Sets the registration endpoint that will be used for creating new Google  Cloud Messaging registrations. | kGCMRegistrationURL |  | ../chromium/src/google_apis/gcm/engine/gservices_switches.cc |
| switch | description | variable | cpp condition | location |
| ------ | ----------- | -------- | ------------- | -------- |
| --enable-gpu-client-logging |  Enable GPU client logging. | kEnableGPUClientLogging |  | ../chromium/src/gpu/command_buffer/client/gpu_switches.cc |
| --enable-gpu-client-tracing |  Enables TRACE for GL calls in the renderer. | kEnableGpuClientTracing |  | ../chromium/src/gpu/command_buffer/client/gpu_switches.cc |
| switch | description | variable | cpp condition | location |
| ------ | ----------- | -------- | ------------- | -------- |
| --compile-shader-always-succeeds |  Always return success when compiling a shader. Linking will still fail. | kCompileShaderAlwaysSucceeds |  | ../chromium/src/gpu/command_buffer/service/gpu_switches.cc |
| --disable-gl-error-limit |  Disable the GL error log limit. | kDisableGLErrorLimit |  | ../chromium/src/gpu/command_buffer/service/gpu_switches.cc |
| --disable-glsl-translator |  Disable the GLSL translator. | kDisableGLSLTranslator |  | ../chromium/src/gpu/command_buffer/service/gpu_switches.cc |
| --disable-shader-name-hashing |  Turn off user-defined name hashing in shaders. | kDisableShaderNameHashing |  | ../chromium/src/gpu/command_buffer/service/gpu_switches.cc |
| --enable-gpu-command-logging |  Turn on Logging GPU commands. | kEnableGPUCommandLogging |  | ../chromium/src/gpu/command_buffer/service/gpu_switches.cc |
| --enable-gpu-debugging |  Turn on Calling GL Error after every command. | kEnableGPUDebugging |  | ../chromium/src/gpu/command_buffer/service/gpu_switches.cc |
| --enable-gpu-service-logging |  Enable GPU service logging. Note: This is the same switch as the one in  gl_switches.cc. It's defined here again to avoid dependencies between  dlls. | kEnableGPUServiceLoggingGPU |  | ../chromium/src/gpu/command_buffer/service/gpu_switches.cc |
| --enable-gpu-driver-debug-logging |  Enable logging of GPU driver debug messages. | kEnableGPUDriverDebugLogging |  | ../chromium/src/gpu/command_buffer/service/gpu_switches.cc |
| --disable-gpu-program-cache |  Turn off gpu program caching | kDisableGpuProgramCache |  | ../chromium/src/gpu/command_buffer/service/gpu_switches.cc |
| --enforce-gl-minimums |  Enforce GL minimums. | kEnforceGLMinimums |  | ../chromium/src/gpu/command_buffer/service/gpu_switches.cc |
| --force-gpu-mem-available-mb |  Sets the total amount of memory that may be allocated for GPU resources | kForceGpuMemAvailableMb |  | ../chromium/src/gpu/command_buffer/service/gpu_switches.cc |
| --force-gpu-mem-discardable-limit-mb |  Sets the maximum GPU memory to use for discardable caches. | kForceGpuMemDiscardableLimitMb |  | ../chromium/src/gpu/command_buffer/service/gpu_switches.cc |
| --force-max-texture-size |  Sets the maximum texture size in pixels. | kForceMaxTextureSize |  | ../chromium/src/gpu/command_buffer/service/gpu_switches.cc |
| --gpu-program-cache-size-kb |  Sets the maximum size of the in-memory gpu program cache, in kb | kGpuProgramCacheSizeKb |  | ../chromium/src/gpu/command_buffer/service/gpu_switches.cc |
| --disable-gpu-shader-disk-cache |  Disables the GPU shader on disk cache. | kDisableGpuShaderDiskCache |  | ../chromium/src/gpu/command_buffer/service/gpu_switches.cc |
| --enable-threaded-texture-mailboxes |  Simulates shared textures when share groups are not available. Not available  everywhere. | kEnableThreadedTextureMailboxes |  | ../chromium/src/gpu/command_buffer/service/gpu_switches.cc |
| --gl-shader-interm-output |  Include ANGLE's intermediate representation (AST) output in shader  compilation info logs. | kGLShaderIntermOutput |  | ../chromium/src/gpu/command_buffer/service/gpu_switches.cc |
| --use-vulkan |  Enable Vulkan support and select Vulkan implementation, must also have  ENABLE_VULKAN defined. This only initializes Vulkan, the flag  --enable-features=Vulkan must also be used to select Vulkan for compositing  and rasterization. | kUseVulkan |  | ../chromium/src/gpu/command_buffer/service/gpu_switches.cc |
| --native |  | kVulkanImplementationNameNative |  | ../chromium/src/gpu/command_buffer/service/gpu_switches.cc |
| --swiftshader |  | kVulkanImplementationNameSwiftshader |  | ../chromium/src/gpu/command_buffer/service/gpu_switches.cc |
| --disable-vulkan-surface |  Disables VK_KHR_surface extension. Instead of using swapchain, bitblt will be  used for present render result on screen. | kDisableVulkanSurface |  | ../chromium/src/gpu/command_buffer/service/gpu_switches.cc |
| switch | description | variable | cpp condition | location |
| ------ | ----------- | -------- | ------------- | -------- |
| --disable-gpu-rasterization |  Disable GPU rasterization, i.e. rasterize on the CPU only.  Overrides the kEnableGpuRasterization flag. | kDisableGpuRasterization |  | ../chromium/src/gpu/config/gpu_switches.cc |
| --disable-mipmap-generation |  Disables mipmap generation in Skia. Used a workaround for select low memory  devices, see https:crbug.com/1138979 for details. | kDisableMipmapGeneration |  | ../chromium/src/gpu/config/gpu_switches.cc |
| --enable-gpu-rasterization |  Allow heuristics to determine when a layer tile should be drawn with the  Skia GPU backend. Only valid with GPU accelerated compositing. | kEnableGpuRasterization |  | ../chromium/src/gpu/config/gpu_switches.cc |
| --gpu-blocklist-test-group |  Select a different set of GPU blocklist entries with the specified  test_group ID. | kGpuBlocklistTestGroup |  | ../chromium/src/gpu/config/gpu_switches.cc |
| --gpu-driver-bug-list-test-group |  Enable an extra set of GPU driver bug list entries with the specified  test_group ID. Note the default test group (group 0) is still active. | kGpuDriverBugListTestGroup |  | ../chromium/src/gpu/config/gpu_switches.cc |
| --gpu-preferences |  Passes encoded GpuPreferences to GPU process. | kGpuPreferences |  | ../chromium/src/gpu/config/gpu_switches.cc |
| --ignore-gpu-blocklist |  Ignores GPU blocklist. | kIgnoreGpuBlocklist |  | ../chromium/src/gpu/config/gpu_switches.cc |
| --gpu-disk-cache-size-kb |  Allows explicitly specifying the shader disk cache size for embedded devices.  Default value is 6MB. On Android, 2MB is default and 128KB for low-end  devices. | kGpuDiskCacheSizeKB |  | ../chromium/src/gpu/config/gpu_switches.cc |
| --disable-gpu-process-for-dx12-info-collection |  Disables the non-sandboxed GPU process for DX12 info collection | kDisableGpuProcessForDX12InfoCollection |  | ../chromium/src/gpu/config/gpu_switches.cc |
| --enable-unsafe-webgpu |  | kEnableUnsafeWebGPU |  | ../chromium/src/gpu/config/gpu_switches.cc |
| --enable-webgpu-developer-features |  Enables WebGPU developer features which are not generally exposed to the web  platform. | kEnableWebGPUDeveloperFeatures |  | ../chromium/src/gpu/config/gpu_switches.cc |
| --enable-dawn-backend-validation |  Enable validation layers in Dawn backends. | kEnableDawnBackendValidation |  | ../chromium/src/gpu/config/gpu_switches.cc |
| --force-webgpu-compat |  Force all WebGPU content to run in WebGPU Compatibility mode. | kForceWebGPUCompat |  | ../chromium/src/gpu/config/gpu_switches.cc |
| --enable-dawn-features |  Set the Dawn features(toggles) enabled on the creation of Dawn devices. | kEnableDawnFeatures |  | ../chromium/src/gpu/config/gpu_switches.cc |
| --disable-dawn-features |  Set the Dawn features(toggles) disabled on the creation of Dawn devices. | kDisableDawnFeatures |  | ../chromium/src/gpu/config/gpu_switches.cc |
| --no-delay-for-dx12-vulkan-info-collection |  Start the non-sandboxed GPU process for DX12 and Vulkan info collection  immediately after the browser starts. The default is to delay for 120  seconds. | kNoDelayForDX12VulkanInfoCollection |  | ../chromium/src/gpu/config/gpu_switches.cc |
| --enable-gpu-blocked-time |  Enables measures of how long GPU Main Thread was blocked between SwapBuffers | kEnableGpuBlockedTime |  | ../chromium/src/gpu/config/gpu_switches.cc |
| --gpu-vendor-id |  Passes the active graphics vendor id from browser process to info collection  GPU process. | kGpuVendorId |  | ../chromium/src/gpu/config/gpu_switches.cc |
| --gpu-device-id |  Passes the active graphics device id from browser process to info collection  GPU process. | kGpuDeviceId |  | ../chromium/src/gpu/config/gpu_switches.cc |
| --gpu-sub-system-id |  Passes the active graphics sub system id from browser process to info  collection GPU process. | kGpuSubSystemId |  | ../chromium/src/gpu/config/gpu_switches.cc |
| --gpu-revision |  Passes the active graphics revision info from browser process to info  collection GPU process. | kGpuRevision |  | ../chromium/src/gpu/config/gpu_switches.cc |
| --gpu-driver-version |  Passes the active graphics driver version from browser process to info  collection GPU process. | kGpuDriverVersion |  | ../chromium/src/gpu/config/gpu_switches.cc |
| --webview-draw-functor-uses-vulkan |  Indicate that the this is being used by Android WebView and its draw functor  is using vulkan. | kWebViewDrawFunctorUsesVulkan |  | ../chromium/src/gpu/config/gpu_switches.cc |
| --enable-vulkan-protected-memory |  Enables using protected memory for vulkan resources. | kEnableVulkanProtectedMemory |  | ../chromium/src/gpu/config/gpu_switches.cc |
| --disable-vulkan-fallback-to-gl-for-testing |  Disables falling back to GL based hardware rendering if initializing Vulkan  fails. This is to allow tests to catch regressions in Vulkan. | kDisableVulkanFallbackToGLForTesting |  | ../chromium/src/gpu/config/gpu_switches.cc |
| --vulkan-heap-memory-limit-mb |  Specifies the heap limit for Vulkan memory.  TODO(crbug.com/40161102): Remove this switch. | kVulkanHeapMemoryLimitMb |  | ../chromium/src/gpu/config/gpu_switches.cc |
| --vulkan-sync-cpu-memory-limit-mb |  Specifies the sync CPU limit for total Vulkan memory.  TODO(crbug.com/40161102): Remove this switch. | kVulkanSyncCpuMemoryLimitMb |  | ../chromium/src/gpu/config/gpu_switches.cc |
| --force-browser-crash-on-gpu-crash |  Crash Chrome if GPU process crashes. This is to force a test to fail when  GPU process crashes unexpectedly. | kForceBrowserCrashOnGpuCrash |  | ../chromium/src/gpu/config/gpu_switches.cc |
| --gpu-watchdog-timeout-seconds |  Override value for the GPU watchdog timeout in seconds. | kGpuWatchdogTimeoutSeconds |  | ../chromium/src/gpu/config/gpu_switches.cc |
| --force-separate-egl-display-for-webgl-testing |  Force the use of a separate EGL display for WebGL contexts. Used for testing  multi-GPU pathways on devices with only one valid GPU. | kForceSeparateEGLDisplayForWebGLTesting |  | ../chromium/src/gpu/config/gpu_switches.cc |
| --skia-graphite-backend |  Specify which backend to use for Skia Graphite - "dawn" (default) or "metal"  (only allowed on non-official developer builds). | kSkiaGraphiteBackend |  | ../chromium/src/gpu/config/gpu_switches.cc |
| --dawn |  | kSkiaGraphiteBackendDawn |  | ../chromium/src/gpu/config/gpu_switches.cc |
| --dawn-d3d11 |  | kSkiaGraphiteBackendDawnD3D11 |  | ../chromium/src/gpu/config/gpu_switches.cc |
| --dawn-d3d12 |  | kSkiaGraphiteBackendDawnD3D12 |  | ../chromium/src/gpu/config/gpu_switches.cc |
| --dawn-metal |  | kSkiaGraphiteBackendDawnMetal |  | ../chromium/src/gpu/config/gpu_switches.cc |
| --dawn-swiftshader |  | kSkiaGraphiteBackendDawnSwiftshader |  | ../chromium/src/gpu/config/gpu_switches.cc |
| --dawn-vulkan |  | kSkiaGraphiteBackendDawnVulkan |  | ../chromium/src/gpu/config/gpu_switches.cc |
| --metal |  | kSkiaGraphiteBackendMetal |  | ../chromium/src/gpu/config/gpu_switches.cc |
| --disable-skia-graphite |  Force disabling/enabling Skia Graphite. Disabling will take precedence over  enabling if both are specified. | kDisableSkiaGraphite |  | ../chromium/src/gpu/config/gpu_switches.cc |
| --enable-skia-graphite |  | kEnableSkiaGraphite |  | ../chromium/src/gpu/config/gpu_switches.cc |
| --shader-cache-path |  | kShaderCachePath |  | ../chromium/src/gpu/config/gpu_switches.cc |
| --use-redist-dml |  Try to use a redistributable DirectML.dll. Used for testing WebNN  against newer DirectML release before it is integrated into Windows OS.  Please see more info about DirectML releases at:  https:learn.microsoft.com/en-us/windows/ai/directml/dml-version-history | kUseRedistributableDirectML |  | ../chromium/src/gpu/config/gpu_switches.cc |
| --enable-gpu-main-time-keeper-metrics |  Enables ThreadControllerWithMessagePumpImpl's TimeKeeper UMA metrics using  CrGpuMain as suffix. | kEnableGpuMainTimeKeeperMetrics |  | ../chromium/src/gpu/config/gpu_switches.cc |
| switch | description | variable | cpp condition | location |
| ------ | ----------- | -------- | ------------- | -------- |
| switch | description | variable | cpp condition | location |
| ------ | ----------- | -------- | ------------- | -------- |
| --disable-ios-password-suggestions |  Disable showing available password credentials in the keyboard accessory  view when focused on form fields. | kDisableIOSPasswordSuggestions |  | ../chromium/src/ios/chrome/browser/flags/chrome_switches.cc |
| --disable-third-party-keyboard-workaround |  Disables the 3rd party keyboard omnibox workaround. | kDisableThirdPartyKeyboardWorkaround |  | ../chromium/src/ios/chrome/browser/flags/chrome_switches.cc |
| --enable-promo-manager-fullscreen-promos |  Enables the Promo Manager to display full-screen promos on app startup. | kEnablePromoManagerFullscreenPromos |  | ../chromium/src/ios/chrome/browser/flags/chrome_switches.cc |
| --enable-ios-handoff-to-other-devices |  Enables support for Handoff from Chrome on iOS to the default browser of  other Apple devices. | kEnableIOSHandoffToOtherDevices |  | ../chromium/src/ios/chrome/browser/flags/chrome_switches.cc |
| --enable-spotlight-actions |  Enables the Spotlight actions. | kEnableSpotlightActions |  | ../chromium/src/ios/chrome/browser/flags/chrome_switches.cc |
| --enable-third-party-keyboard-workaround |  Enables the 3rd party keyboard omnibox workaround. | kEnableThirdPartyKeyboardWorkaround |  | ../chromium/src/ios/chrome/browser/flags/chrome_switches.cc |
| --enable-discover-feed |  Enabled the NTP Discover feed. | kEnableDiscoverFeed |  | ../chromium/src/ios/chrome/browser/flags/chrome_switches.cc |
| --enable-upgrade-signin-promo |  Enables the upgrade sign-in promo. | kEnableUpgradeSigninPromo |  | ../chromium/src/ios/chrome/browser/flags/chrome_switches.cc |
| --force-device-switcher-experience |  Enables device switcher experience for the segment specified in the argument,  e.g. "Android." | kForceDeviceSwitcherExperienceCommandLineFlag |  | ../chromium/src/ios/chrome/browser/flags/chrome_switches.cc |
| --force-shopper-experience |  Enables shopping feature user experience for the segment specified in the  argument, e.g. "ShoppingUser" or "Other". | kForceShopperExperience |  | ../chromium/src/ios/chrome/browser/flags/chrome_switches.cc |
| --user-agent |  A string used to override the default user agent with a custom one. | kUserAgent |  | ../chromium/src/ios/chrome/browser/flags/chrome_switches.cc |
| switch | description | variable | cpp condition | location |
| ------ | ----------- | -------- | ------------- | -------- |
| --disable-all-injected-scripts |  Prevents the injection of all Javascript injected through JavaScriptFeatures. | kDisableAllInjectedScripts |  | ../chromium/src/ios/web/switches.cc |
| --disable-injected-feature-scripts |  Prevents most injection of Javascript injected through JavaScriptFeatures,  however basic shared scripts which setup WebFrames are still injected. | kDisableInjectedFeatureScripts |  | ../chromium/src/ios/web/switches.cc |
| --disable-listed-scripts |  Prevents the listed scripts from being injected. The value must be a comma  separated string of `injection_token_`s from the JavaScriptFeatures to be  disabled.  For example, to disable context menu JS, use:  `--disable-listed-scripts=all_frames_context_menu,main_frame_context_menu` | kDisableListedScripts |  | ../chromium/src/ios/web/switches.cc |
| --enable-listed-scripts |  Enables only the listed scripts. The value must be a comma separated string  of `injection_token_`s from the JavaScriptFeatures to be enabled.  For example, to only enable context menu JS, use:  `--enable-listed-scripts=gcrweb,common,message,all_frames_context_menu,      main_frame_context_menu`  Note that all dependencies, must be manually enabled when using this flag. | kEnableListedScripts |  | ../chromium/src/ios/web/switches.cc |
| --disable-listed-javascript-features |  Disables the listed JavaScriptFeature instances. The value must be a  comma separated string of the value returned by  `JavaScriptFeature::GetScriptMessageHandlerName()`.  For example, to disable ContextMenuJavaScriptFeature, use:  `--disable-listed-javascript-features=FindElementResultHandler` | kDisableListedJavascriptFeatures |  | ../chromium/src/ios/web/switches.cc |
| --enable-listed-javascript-features |  Enables only the listed JavaScriptFeature instances. The value must be a  comma separated string of the value returned by  `JavaScriptFeature::GetScriptMessageHandlerName()`. If a feature does not  have a message handler, it will NOT be enabled when using this flag. However,  the features returned by `GetBaseJavaScriptFeature()`,  `GetCommonJavaScriptFeature()` and `GetMessageJavaScriptFeature()` are always  enabled (even though they do not have message handlers) because most features  rely on them and there would otherwise be no way to enable them.  For example, to only enable only ContextMenuJavaScriptFeature, use:  `--enable-listed-javascript-features=FindElementResultHandler` | kEnableListedJavascriptFeatures |  | ../chromium/src/ios/web/switches.cc |
| switch | description | variable | cpp condition | location |
| ------ | ----------- | -------- | ------------- | -------- |
| --audio-buffer-size |  Allow users to specify a custom buffer size for debugging purpose. | kAudioBufferSize |  | ../chromium/src/media/base/media_switches.cc |
| --audio-codecs-from-edid |  Audio codecs supported by the HDMI sink is retrieved from the audio  service process. EDID contains the Short Audio Descriptors, which list  the audio decoders supported, and the information is presented as a  bitmask of supported audio codecs. | kAudioCodecsFromEDID | BUILDFLAG(ENABLE_PASSTHROUGH_AUDIO_CODECS) | ../chromium/src/media/base/media_switches.cc |
| --autoplay-policy |  Command line flag name to set the autoplay policy. | kAutoplayPolicy |  | ../chromium/src/media/base/media_switches.cc |
| --disable-audio-input |  Forces input and output stream creation to use fake audio streams. | kDisableAudioInput |  | ../chromium/src/media/base/media_switches.cc |
| --disable-audio-output |  | kDisableAudioOutput |  | ../chromium/src/media/base/media_switches.cc |
| --fail-audio-stream-creation |  Causes the AudioManager to fail creating audio streams. Used when testing  various failure cases. | kFailAudioStreamCreation |  | ../chromium/src/media/base/media_switches.cc |
| --video-threads |  Set number of threads to use for video decoding. | kVideoThreads |  | ../chromium/src/media/base/media_switches.cc |
| --disable-background-media-suspend |  Do not immediately suspend media in background tabs. | kDisableBackgroundMediaSuspend |  | ../chromium/src/media/base/media_switches.cc |
| --report-vp9-as-an-unsupported-mime-type |  Force to report VP9 as an unsupported MIME type. | kReportVp9AsAnUnsupportedMimeType |  | ../chromium/src/media/base/media_switches.cc |
| --alsa-input-device |  The Alsa device to use when opening an audio input stream. | kAlsaInputDevice | BUILDFLAG(IS_LINUX) || BUILDFLAG(IS_CHROMEOS) || BUILDFLAG(IS_FREEBSD) ||     BUILDFLAG(IS_SOLARIS) | ../chromium/src/media/base/media_switches.cc |
| --alsa-output-device |  The Alsa device to use when opening an audio stream. | kAlsaOutputDevice | BUILDFLAG(IS_LINUX) || BUILDFLAG(IS_CHROMEOS) || BUILDFLAG(IS_FREEBSD) ||     BUILDFLAG(IS_SOLARIS) | ../chromium/src/media/base/media_switches.cc |
| --enable-exclusive-audio |  Use exclusive mode audio streaming for Windows Vista and higher.  Leads to lower latencies for audio streams which uses the  AudioParameters::AUDIO_PCM_LOW_LATENCY audio path.  See http:msdn.microsoft.com/en-us/library/windows/desktop/dd370844.aspx  for details. | kEnableExclusiveAudio | BUILDFLAG(IS_WIN) | ../chromium/src/media/base/media_switches.cc |
| --force-wave-audio |  Use Windows WaveOut/In audio API even if Core Audio is supported. | kForceWaveAudio | BUILDFLAG(IS_WIN) | ../chromium/src/media/base/media_switches.cc |
| --try-supported-channel-layouts |  Instead of always using the hardware channel layout, check if a driver  supports the source channel layout.  Avoids outputting empty channels and  permits drivers to enable stereo to multichannel expansion.  Kept behind a  flag since some drivers lie about supported layouts and hang when used.  See  http:crbug.com/259165 for more details. | kTrySupportedChannelLayouts | BUILDFLAG(IS_WIN) | ../chromium/src/media/base/media_switches.cc |
| --waveout-buffers |  Number of buffers to use for WaveOut. | kWaveOutBuffers | BUILDFLAG(IS_WIN) | ../chromium/src/media/base/media_switches.cc |
| --enable-protected-video-buffers |  Enables protected buffers for encrypted video streams. | kEnableProtectedVideoBuffers | BUILDFLAG(IS_FUCHSIA) | ../chromium/src/media/base/media_switches.cc |
| --force-protected-video-output-buffers |  Forces protected memory for all output video buffers generated by  FuchsiaVideoDecoder, including unencrypted streams. Ignored unless  --enable-protected-video-buffers is also specified. | kForceProtectedVideoOutputBuffers | BUILDFLAG(IS_FUCHSIA) | ../chromium/src/media/base/media_switches.cc |
| --min-video-decoder-output-buffer-size |  Minimum size for buffer size used for output video frames in  FuchsiaVideoDecoder. May be set to avoid re-allocating video buffers when an  application upgrades video resolution mid-stream. | kMinVideoDecoderOutputBufferSize | BUILDFLAG(IS_FUCHSIA) | ../chromium/src/media/base/media_switches.cc |
| --audio-capturer-with-echo-cancellation |  Forces AudioManagerFuchsia to assume that the AudioCapturer implements echo  cancellation.  TODO(crbug.com/42050621): Remove this once AudioManagerFuchsia is updated to  get this information from AudioCapturerFactory. | kAudioCapturerWithEchoCancellation | BUILDFLAG(IS_FUCHSIA) | ../chromium/src/media/base/media_switches.cc |
| --use-cras |  Use CRAS, the ChromeOS audio server. | kUseCras | BUILDFLAG(USE_CRAS) | ../chromium/src/media/base/media_switches.cc |
| --system-aec-enabled |  Enforce system audio echo cancellation. | kSystemAecEnabled | BUILDFLAG(USE_CRAS) | ../chromium/src/media/base/media_switches.cc |
| --unsafely-allow-protected-media-identifier-for-domain |  For automated testing of protected content, this switch allows specific  domains (e.g. example.com) to always allow the permission to share the  protected media identifier. In this context, domain does not include the  port number. User's content settings will not be affected by enabling this  switch.  Reference: http:crbug.com/718608  Example:  --unsafely-allow-protected-media-identifier-for-domain=a.com,b.ca | kUnsafelyAllowProtectedMediaIdentifierForDomain |  | ../chromium/src/media/base/media_switches.cc |
| --auto-grant-captured-surface-control-prompt |  Skip the permission prompt for Captured Surface Control. | kAutoGrantCapturedSurfaceControlPrompt |  | ../chromium/src/media/base/media_switches.cc |
| --use-fake-device-for-media-stream |  Use fake device for Media Stream to replace actual camera and microphone.  For the list of allowed parameters, see  FakeVideoCaptureDeviceFactory::ParseFakeDevicesConfigFromOptionsString(). | kUseFakeDeviceForMediaStream |  | ../chromium/src/media/base/media_switches.cc |
| --use-file-for-fake-video-capture |  Use an .y4m file to play as the webcam. See the comments in  media/capture/video/file_video_capture_device.h for more details. | kUseFileForFakeVideoCapture |  | ../chromium/src/media/base/media_switches.cc |
| --use-file-for-fake-audio-capture |  Play a .wav file as the microphone. Note that for WebRTC calls we'll treat  the bits as if they came from the microphone, which means you should disable  audio processing (lest your audio file will play back distorted). The input  file is converted to suit Chrome's audio buses if necessary, so most sane  .wav files should work. You can pass either <path> to play the file looping  or <path>%noloop to stop after playing the file to completion.   Must also be used with kDisableAudioInput or kUseFakeDeviceForMediaStream. | kUseFileForFakeAudioCapture |  | ../chromium/src/media/base/media_switches.cc |
| --use-fake-mjpeg-decode-accelerator |  Use a fake device for accelerated decoding of MJPEG. This allows, for  example, testing of the communication to the GPU service without requiring  actual accelerator hardware to be present. | kUseFakeMjpegDecodeAccelerator |  | ../chromium/src/media/base/media_switches.cc |
| --disable-accelerated-mjpeg-decode |  Disable hardware acceleration of mjpeg decode for captured frame, where  available. | kDisableAcceleratedMjpegDecode |  | ../chromium/src/media/base/media_switches.cc |
| --mute-audio |  Mutes audio sent to the audio device so it is not audible during  automated testing. | kMuteAudio |  | ../chromium/src/media/base/media_switches.cc |
| --disable-rtc-smoothness-algorithm |  Disables the new rendering algorithm for webrtc, which is designed to improve  the rendering smoothness. | kDisableRTCSmoothnessAlgorithm |  | ../chromium/src/media/base/media_switches.cc |
| --force-video-overlays |  Force media player using SurfaceView instead of SurfaceTexture on Android. | kForceVideoOverlays |  | ../chromium/src/media/base/media_switches.cc |
| --mse-audio-buffer-size-limit-mb |  Allows explicitly specifying MSE audio/video buffer sizes as megabytes.  Default values are 150M for video and 12M for audio. | kMSEAudioBufferSizeLimitMb |  | ../chromium/src/media/base/media_switches.cc |
| --mse-video-buffer-size-limit-mb |  | kMSEVideoBufferSizeLimitMb |  | ../chromium/src/media/base/media_switches.cc |
| --clear-key-cdm-path-for-testing |  Specifies the path to the Clear Key CDM for testing, which is necessary to  support External Clear Key key system when library CDM is enabled. Note that  External Clear Key key system support is also controlled by feature  kExternalClearKeyForTesting. | kClearKeyCdmPathForTesting |  | ../chromium/src/media/base/media_switches.cc |
| --override-enabled-cdm-interface-version |  Overrides the default enabled library CDM interface version(s) with the one  specified with this switch, which will be the only version enabled. For  example, on a build where CDM 8, CDM 9 and CDM 10 are all supported  (implemented), but only CDM 8 and CDM 9 are enabled by default:   --override-enabled-cdm-interface-version=8 : Only CDM 8 is enabled   --override-enabled-cdm-interface-version=9 : Only CDM 9 is enabled   --override-enabled-cdm-interface-version=10 : Only CDM 10 is enabled   --override-enabled-cdm-interface-version=11 : No CDM interface is enabled  This can be used for local testing and debugging. It can also be used to  enable an experimental CDM interface (which is always disabled by default)  for testing while it's still in development. | kOverrideEnabledCdmInterfaceVersion |  | ../chromium/src/media/base/media_switches.cc |
| --override-hardware-secure-codecs-for-testing |  Overrides hardware secure codecs support for testing. If specified, real  platform hardware secure codecs check will be skipped. Valid codecs are:  - video: "vp8", "vp9", "avc1", "hevc", "dolbyvision", "av01"  - video that does not support clear lead: `<video>-no-clearlead`, where    <video> is from the list above.  - audio: "mp4a", "vorbis"  Codecs are separated by comma. For example:   --override-hardware-secure-codecs-for-testing=vp8,vp9-no-clearlead,vorbis   --override-hardware-secure-codecs-for-testing=avc1,mp4a  CENC encryption scheme is assumed to be supported for the specified codecs.  If no valid codecs specified, no hardware secure codecs are supported. This  can be used to disable hardware secure codecs support:   --override-hardware-secure-codecs-for-testing | kOverrideHardwareSecureCodecsForTesting |  | ../chromium/src/media/base/media_switches.cc |
| --enable-live-caption-pref-for-testing |  Sets the default value for the kLiveCaptionEnabled preference to true. | kEnableLiveCaptionPrefForTesting |  | ../chromium/src/media/base/media_switches.cc |
| --allow-ra-in-dev-mode |  Allows remote attestation (RA) in dev mode for testing purpose. Usually RA  is disabled in dev mode because it will always fail. However, there are cases  in testing where we do want to go through the permission flow even in dev  mode. This can be enabled by this flag. | kAllowRAInDevMode | BUILDFLAG(IS_CHROMEOS) | ../chromium/src/media/base/media_switches.cc |
| --cros-bundled-widevine |  These flags are passed from ash-chrome to lacros-chrome that correspond to  the directories used for the Widevine CDM (the bundled CDM and the Component  Updated CDM). | kCrosWidevineBundledDir | BUILDFLAG(IS_CHROMEOS) | ../chromium/src/media/base/media_switches.cc |
| --cros-component-updated-widevine-hint-file |  | kCrosWidevineComponentUpdatedHintFile | BUILDFLAG(IS_CHROMEOS) | ../chromium/src/media/base/media_switches.cc |
| --hardware-video-decode-framerate |  Some (Qualcomm only at the moment) V4L2 video decoders require setting the  framerate so that the hardware decoder can scale the clocks efficiently.  This provides a mechanism during testing to lock the decoder framerate  to a specific value. | kHardwareVideoDecodeFrameRate | BUILDFLAG(USE_CHROMEOS_MEDIA_ACCELERATION) | ../chromium/src/media/base/media_switches.cc |
| --enable-primary-node-access-for-vkms-testing |  This is needed for V4L2 testing using VISL (virtual driver) on cros VM with  arm64-generic-vm. Minigbm buffer allocation is done using dumb driver with  vkms. | kEnablePrimaryNodeAccessForVkmsTesting | BUILDFLAG(USE_V4L2_CODEC) | ../chromium/src/media/base/media_switches.cc |
| --cast-streaming-force-disable-hardware-h264 |  | kCastStreamingForceDisableHardwareH264 |  | ../chromium/src/media/base/media_switches.cc |
| --cast-streaming-force-disable-hardware-vp8 |  | kCastStreamingForceDisableHardwareVp8 |  | ../chromium/src/media/base/media_switches.cc |
| --cast-streaming-force-disable-hardware-vp9 |  | kCastStreamingForceDisableHardwareVp9 |  | ../chromium/src/media/base/media_switches.cc |
| --cast-streaming-force-enable-hardware-h264 |  | kCastStreamingForceEnableHardwareH264 |  | ../chromium/src/media/base/media_switches.cc |
| --cast-streaming-force-enable-hardware-vp8 |  | kCastStreamingForceEnableHardwareVp8 |  | ../chromium/src/media/base/media_switches.cc |
| --cast-streaming-force-enable-hardware-vp9 |  | kCastStreamingForceEnableHardwareVp9 |  | ../chromium/src/media/base/media_switches.cc |
| switch | description | variable | cpp condition | location |
| ------ | ----------- | -------- | ------------- | -------- |
| --video-capture-use-gpu-memory-buffer |  Enables GpuMemoryBuffer-based buffer pool. | kVideoCaptureUseGpuMemoryBuffer |  | ../chromium/src/media/capture/capture_switches.cc |
| --disable-video-capture-use-gpu-memory-buffer |  This is for the same feature controlled by kVideoCaptureUseGpuMemoryBuffer.  kVideoCaptureUseGpuMemoryBuffer is settled by chromeos overlays. This flag is  necessary to overwrite the settings via chrome: flag. The behavior of  chrome:flag#zero-copy-video-capture is as follows;  Default  : Respect chromeos overlays settings.  Enabled  : Force to enable kVideoCaptureUseGpuMemoryBuffer.  Disabled : Force to disable kVideoCaptureUseGpuMemoryBuffer. | kDisableVideoCaptureUseGpuMemoryBuffer |  | ../chromium/src/media/capture/capture_switches.cc |
| switch | description | variable | cpp condition | location |
| ------ | ----------- | -------- | ------------- | -------- |
| switch | description | variable | cpp condition | location |
| ------ | ----------- | -------- | ------------- | -------- |
| switch | description | variable | cpp condition | location |
| ------ | ----------- | -------- | ------------- | -------- |
| --mojo-is-broker |  Forces the process's global Mojo node to be configured as a broker. Only  honored for test runners using MojoTestSuiteBase. | kMojoIsBroker |  | ../chromium/src/mojo/core/test/test_switches.cc |
| --no-mojo |  Disables Mojo initialization completely in the process. Only applies to  test child processes. See base::MultiprocessTest. | kNoMojo |  | ../chromium/src/mojo/core/test/test_switches.cc |
| switch | description | variable | cpp condition | location |
| ------ | ----------- | -------- | ------------- | -------- |
| --legacy-client-fd |  The integer value of a file descriptor inherited by the mojo_proxy process  when launched by its host. This descriptor references a Unix socket which is  connected to the legacy client application to be the target of this proxy.  Required. | kLegacyClientFd |  | ../chromium/src/mojo/proxy/switches.cc |
| --host-ipcz-transport-fd |  The integer value of a file descriptor inherited by the mojo_proxy process  when launched by its host. This descriptor references a Unix socket which is  connected to the host process which launched this proxy to sit between the  host and some legacy client application.  Required. | kHostIpczTransportFd |  | ../chromium/src/mojo/proxy/switches.cc |
| --inherit-ipcz-broker |  By default, mojo_proxy assumes its host is a broker. When this flag is given  it instead assumes its host is a non-broker who is offering to share their  broker. The proxy must be configured correctly in this regard or all  connections through it will fail. | kInheritIpczBroker |  | ../chromium/src/mojo/proxy/switches.cc |
| --attachment-name |  For client applications who expect a single Mojo invitation attachment with a  free-form name assigned to it, this specifies that attachment name. Either  this or kNumericAttachmentNames must be specified on the command line. | kAttachmentName |  | ../chromium/src/mojo/proxy/switches.cc |
| --num-attachments |  For client applications who expect Mojo invitation attachments to be assigned  zero-based 64-bit integral values, this specifies the number of in-use  attachments. The names are implicitly sequental integers starting from 0. | kNumAttachments |  | ../chromium/src/mojo/proxy/switches.cc |
| switch | description | variable | cpp condition | location |
| ------ | ----------- | -------- | ------------- | -------- |
| switch | description | variable | cpp condition | location |
| ------ | ----------- | -------- | ------------- | -------- |
| switch | description | variable | cpp condition | location |
| ------ | ----------- | -------- | ------------- | -------- |
| switch | description | variable | cpp condition | location |
| ------ | ----------- | -------- | ------------- | -------- |
| switch | description | variable | cpp condition | location |
| ------ | ----------- | -------- | ------------- | -------- |
| switch | description | variable | cpp condition | location |
| ------ | ----------- | -------- | ------------- | -------- |
| switch | description | variable | cpp condition | location |
| ------ | ----------- | -------- | ------------- | -------- |
| --enable-pepper-testing |  Enables the testing interface for PPAPI. | kEnablePepperTesting |  | ../chromium/src/ppapi/shared_impl/ppapi_switches.cc |
| switch | description | variable | cpp condition | location |
| ------ | ----------- | -------- | ------------- | -------- |
| switch | description | variable | cpp condition | location |
| ------ | ----------- | -------- | ------------- | -------- |
| --service-sandbox-type |  Type of sandbox to apply to the process running the service, one of the  values in the next block. | kServiceSandboxType |  | ../chromium/src/sandbox/policy/switches.cc |
| --none |  Must be in sync with "sandbox_type" values as used in service manager's  manifest.json catalog files. | kNoneSandbox |  | ../chromium/src/sandbox/policy/switches.cc |
| --none_and_elevated |  | kNoneSandboxAndElevatedPrivileges |  | ../chromium/src/sandbox/policy/switches.cc |
| --network |  | kNetworkSandbox |  | ../chromium/src/sandbox/policy/switches.cc |
| --on_device_model_execution |  | kOnDeviceModelExecutionSandbox |  | ../chromium/src/sandbox/policy/switches.cc |
| --ppapi |  | kPpapiPluginProcess |  | ../chromium/src/sandbox/policy/switches.cc |
| --utility |  | kUtilityProcess |  | ../chromium/src/sandbox/policy/switches.cc |
| --cdm |  | kCdmSandbox |  | ../chromium/src/sandbox/policy/switches.cc |
| --print_backend |  | kPrintBackendSandbox | BUILDFLAG(ENABLE_PRINTING) | ../chromium/src/sandbox/policy/switches.cc |
| --print_compositor |  | kPrintCompositorSandbox |  | ../chromium/src/sandbox/policy/switches.cc |
| --audio |  | kAudioSandbox |  | ../chromium/src/sandbox/policy/switches.cc |
| --service |  | kServiceSandbox |  | ../chromium/src/sandbox/policy/switches.cc |
| --service_with_jit |  | kServiceSandboxWithJit |  | ../chromium/src/sandbox/policy/switches.cc |
| --screen_ai |  | kScreenAISandbox | BUILDFLAG(ENABLE_SCREEN_AI_SERVICE) | ../chromium/src/sandbox/policy/switches.cc |
| --video_effects |  | kVideoEffectsSandbox |  | ../chromium/src/sandbox/policy/switches.cc |
| --speech_recognition |  | kSpeechRecognitionSandbox |  | ../chromium/src/sandbox/policy/switches.cc |
| --video_capture |  | kVideoCaptureSandbox |  | ../chromium/src/sandbox/policy/switches.cc |
| --pdf_conversion |  | kPdfConversionSandbox | BUILDFLAG(IS_WIN) | ../chromium/src/sandbox/policy/switches.cc |
| --xr_compositing |  | kXrCompositingSandbox | BUILDFLAG(IS_WIN) | ../chromium/src/sandbox/policy/switches.cc |
| --icon_reader |  | kIconReaderSandbox | BUILDFLAG(IS_WIN) | ../chromium/src/sandbox/policy/switches.cc |
| --mf_cdm |  | kMediaFoundationCdmSandbox | BUILDFLAG(IS_WIN) | ../chromium/src/sandbox/policy/switches.cc |
| --proxy_resolver_win |  | kWindowsSystemProxyResolverSandbox | BUILDFLAG(IS_WIN) | ../chromium/src/sandbox/policy/switches.cc |
| --mirroring |  | kMirroringSandbox | BUILDFLAG(IS_MAC) | ../chromium/src/sandbox/policy/switches.cc |
| --hardware_video_decoding |  | kHardwareVideoDecodingSandbox | BUILDFLAG(IS_LINUX) || BUILDFLAG(IS_CHROMEOS_ASH) | ../chromium/src/sandbox/policy/switches.cc |
| --hardware_video_encoding |  | kHardwareVideoEncodingSandbox | BUILDFLAG(IS_LINUX) || BUILDFLAG(IS_CHROMEOS) | ../chromium/src/sandbox/policy/switches.cc |
| --ime |  | kImeSandbox | BUILDFLAG(IS_CHROMEOS_ASH) | ../chromium/src/sandbox/policy/switches.cc |
| --tts |  | kTtsSandbox | BUILDFLAG(IS_CHROMEOS_ASH) | ../chromium/src/sandbox/policy/switches.cc |
| --nearby |  | kNearbySandbox | BUILDFLAG(IS_CHROMEOS_ASH) | ../chromium/src/sandbox/policy/switches.cc |
| --allow-sandbox-debugging |  Allows debugging of sandboxed processes (see zygote_main_linux.cc). | kAllowSandboxDebugging |  | ../chromium/src/sandbox/policy/switches.cc |
| --disable-gpu-sandbox |  Disables the GPU process sandbox. | kDisableGpuSandbox |  | ../chromium/src/sandbox/policy/switches.cc |
| --disable-namespace-sandbox |  Disables usage of the namespace sandbox. | kDisableNamespaceSandbox |  | ../chromium/src/sandbox/policy/switches.cc |
| --disable-seccomp-filter-sandbox |  Disable the seccomp filter sandbox (seccomp-bpf) (Linux only). | kDisableSeccompFilterSandbox |  | ../chromium/src/sandbox/policy/switches.cc |
| --disable-setuid-sandbox |  Disable the setuid sandbox (Linux only). | kDisableSetuidSandbox |  | ../chromium/src/sandbox/policy/switches.cc |
| --gpu-sandbox-allow-sysv-shm |  Allows shmat() system call in the GPU sandbox. | kGpuSandboxAllowSysVShm |  | ../chromium/src/sandbox/policy/switches.cc |
| --gpu-sandbox-failures-fatal |  Makes GPU sandbox failures fatal. | kGpuSandboxFailuresFatal |  | ../chromium/src/sandbox/policy/switches.cc |
| --no-sandbox |  Disables the sandbox for all process types that are normally sandboxed.  Meant to be used as a browser-level switch for testing purposes only. | kNoSandbox |  | ../chromium/src/sandbox/policy/switches.cc |
| --no-zygote-sandbox |  Instructs the zygote to launch without a sandbox. Processes forked from this  type of zygote will apply their own custom sandboxes later. | kNoZygoteSandbox | BUILDFLAG(IS_LINUX) || BUILDFLAG(IS_CHROMEOS) | ../chromium/src/sandbox/policy/switches.cc |
| --allow-third-party-modules |  Allows third party modules to inject by disabling the BINARY_SIGNATURE  mitigation policy on Win10+. Also has other effects in ELF. | kAllowThirdPartyModules | BUILDFLAG(IS_WIN) | ../chromium/src/sandbox/policy/switches.cc |
| --add-gpu-appcontainer-caps |  Add additional capabilities to the AppContainer sandbox on the GPU process. | kAddGpuAppContainerCaps | BUILDFLAG(IS_WIN) | ../chromium/src/sandbox/policy/switches.cc |
| --add-xr-appcontainer-caps |  Add additional capabilities to the AppContainer sandbox used for XR  compositing. | kAddXrAppContainerCaps | BUILDFLAG(IS_WIN) | ../chromium/src/sandbox/policy/switches.cc |
| --enable-sandbox-logging |  Cause the OS X sandbox write to syslog every time an access to a resource  is denied by the sandbox. | kEnableSandboxLogging | BUILDFLAG(IS_MAC) | ../chromium/src/sandbox/policy/switches.cc |
| --disable-metal-shader-cache |  Disables Metal's shader cache, using the GPU sandbox to prevent access to it. | kDisableMetalShaderCache | BUILDFLAG(IS_MAC) | ../chromium/src/sandbox/policy/switches.cc |
| --type |  Flags spied upon from other layers. | kProcessType |  | ../chromium/src/sandbox/policy/switches.cc |
| --gpu-process |  | kGpuProcess |  | ../chromium/src/sandbox/policy/switches.cc |
| --nacl-loader |  | kNaClLoaderProcess |  | ../chromium/src/sandbox/policy/switches.cc |
| --renderer |  | kRendererProcess |  | ../chromium/src/sandbox/policy/switches.cc |
| --zygote |  | kZygoteProcessType |  | ../chromium/src/sandbox/policy/switches.cc |
| --relauncher |  | kRelauncherProcessType |  | ../chromium/src/sandbox/policy/switches.cc |
| --code-sign-clone-cleanup |  | kCodeSignCloneCleanupProcessType |  | ../chromium/src/sandbox/policy/switches.cc |
| switch | description | variable | cpp condition | location |
| ------ | ----------- | -------- | ------------- | -------- |
| --disable-hid-blocklist |  Disable the HID blocklist. | kDisableHidBlocklist |  | ../chromium/src/services/device/public/cpp/hid/hid_switches.cc |
| switch | description | variable | cpp condition | location |
| ------ | ----------- | -------- | ------------- | -------- |
| --force-effective-connection-type |  Forces Network Quality Estimator (NQE) to return a specific effective  connection type. | kForceEffectiveConnectionType |  | ../chromium/src/services/network/public/cpp/network_switches.cc |
| --host-resolver-rules |  These mappings only apply to the host resolver. | kHostResolverRules |  | ../chromium/src/services/network/public/cpp/network_switches.cc |
| --ignore-certificate-errors-spki-list |  A set of public key hashes for which to ignore certificate-related errors.   If the certificate chain presented by the server does not validate, and one  or more certificates have public key hashes that match a key from this list,  the error is ignored.   The switch value must be a comma-separated list of Base64-encoded SHA-256  SPKI Fingerprints (RFC 7469, Section 2.4).   This switch has no effect unless --user-data-dir (as defined by the content  embedder) is also present. | kIgnoreCertificateErrorsSPKIList |  | ../chromium/src/services/network/public/cpp/network_switches.cc |
| --log-net-log |  Enables saving net log events to a file. If a value is given, it used as the  path the the file, otherwise the file is named netlog.json and placed in the  user data directory. | kLogNetLog |  | ../chromium/src/services/network/public/cpp/network_switches.cc |
| --net-log-capture-mode |  Sets the granularity of events to capture in the network log. The mode can be  set to one of the following values:    "Default"    "IncludeSensitive"    "Everything"   See the enums of the corresponding name in net_log_capture_mode.h for a  description of their meanings. | kNetLogCaptureMode |  | ../chromium/src/services/network/public/cpp/network_switches.cc |
| --net-log-max-size-mb |  Sets the maximum size, in megabytes. The log file can grow to before older  data is overwritten. Do not use this flag if you want an unlimited file size. | kNetLogMaxSizeMb |  | ../chromium/src/services/network/public/cpp/network_switches.cc |
| --ssl-key-log-file |  Causes SSL key material to be logged to the specified file for debugging  purposes. See  https:developer.mozilla.org/en-US/docs/Mozilla/Projects/NSS/Key_Log_Format  for the format. | kSSLKeyLogFile |  | ../chromium/src/services/network/public/cpp/network_switches.cc |
| --test-third-party-cookie-phaseout |  | kTestThirdPartyCookiePhaseout |  | ../chromium/src/services/network/public/cpp/network_switches.cc |
| --unsafely-treat-insecure-origin-as-secure |  Treat given (insecure) origins as secure origins. Multiple origins can be  supplied as a comma-separated list. For the definition of secure contexts,  see https:w3c.github.io/webappsec-secure-contexts/ and  https:www.w3.org/TR/powerful-features/#is-origin-trustworthy   Example:  --unsafely-treat-insecure-origin-as-secure=http:a.test,http:b.test | kUnsafelyTreatInsecureOriginAsSecure |  | ../chromium/src/services/network/public/cpp/network_switches.cc |
| --additional-private-state-token-key-commitments |  Manually sets additional Private State Tokens key commitments in the network  service to the given value, which should be a JSON dictionary satisfying the  requirements of TrustTokenKeyCommitmentParser::ParseMultipleIssuers.   These keys are available in addition to keys provided by the most recent call  to TrustTokenKeyCommitments::Set.   For issuers with keys provided through both the command line and  TrustTokenKeyCommitments::Set, the keys provided through the command line  take precedence. This is because someone testing manually might want to pass  additional keys via the command line to a real Chrome release with the  component updater enabled, and it would be surprising if the manually-passed  keys were overwritten some time after startup when the component updater  runs. | kAdditionalTrustTokenKeyCommitments |  | ../chromium/src/services/network/public/cpp/network_switches.cc |
| --use-first-party-set |  Allows the manual specification of a First-Party Set, as a comma-separated  list of origins. The first origin in the list is treated as the owner of the  set.  DEPRECATED(crbug.com/1486689): This switch is under deprecation due to  renaming "First-Party Set" to "Related Website Set". Please use  `kUseRelatedWebsiteSet` instead. | kUseFirstPartySet |  | ../chromium/src/services/network/public/cpp/network_switches.cc |
| --use-related-website-set |  Allows the manual specification of a Related Website Set, as a  comma-separated list of origins. The first origin in the list is treated as  the primary site of the set. | kUseRelatedWebsiteSet |  | ../chromium/src/services/network/public/cpp/network_switches.cc |
| --ip-address-space-overrides |  Specifies manual overrides to the IP endpoint -> IP address space mapping.  This allows running local tests against "public" and "private" IP addresses.   This switch is specified as a comma-separated list of overrides. Each  override is given as a colon-separated "<endpoint>:<address space>" pair.  Grammar, in pseudo-BNF format:     switch := override-list    override-list := override “,” override-list | <nil>    override := ip-endpoint “=” address-space    address-space := “public” | “private” | “local”    ip-endpoint := ip-address ":" port    ip-address := see `net::ParseURLHostnameToAddress()` for details    port := integer in the [0-65535] range   Any invalid entries in the comma-separated list are ignored.   See also the design doc:  https:docs.google.com/document/d/1-umCGylIOuSG02k9KGDwKayt3bzBXtGwVlCQHHkIcnQ/edit#   And the Web Platform Test RFC #72 behind it:  https:github.com/web-platform-tests/rfcs/blob/master/rfcs/address_space_overrides.md | kIpAddressSpaceOverrides |  | ../chromium/src/services/network/public/cpp/network_switches.cc |
| switch | description | variable | cpp condition | location |
| ------ | ----------- | -------- | ------------- | -------- |
| --disable-chrome-tracing-computation |  Disable the tracing service graph compuation while writing the trace. | kDisableChromeTracingComputation |  | ../chromium/src/services/resource_coordinator/memory_instrumentation/switches.cc |
| --use-heap-profiling-proto-writer |  | kUseHeapProfilingProtoWriter |  | ../chromium/src/services/resource_coordinator/memory_instrumentation/switches.cc |
| switch | description | variable | cpp condition | location |
| ------ | ----------- | -------- | ------------- | -------- |
| --service-name |  Indicates the name of the service to run. Useful for debugging, or if a  service executable is built to support being run as a number of potential  different services. | kServiceName |  | ../chromium/src/services/service_manager/public/cpp/service_executable/switches.cc |
| --service-request-attachment-name |  The name of the |mojo::PendingReceiver<service_manager::mojom::Service>|  message pipe handle that is attached to the incoming Mojo invitation received  by the service. | kServiceRequestAttachmentName |  | ../chromium/src/services/service_manager/public/cpp/service_executable/switches.cc |
| switch | description | variable | cpp condition | location |
| ------ | ----------- | -------- | ------------- | -------- |
| --enable-service-manager-tracing |  Enable the tracing service. | kEnableTracing |  | ../chromium/src/services/service_manager/switches.cc |
| switch | description | variable | cpp condition | location |
| ------ | ----------- | -------- | ------------- | -------- |
| --text-contrast |  | kTextContrast |  | ../chromium/src/skia/ext/switches.cc |
| --text-gamma |  | kTextGamma |  | ../chromium/src/skia/ext/switches.cc |
| switch | description | variable | cpp condition | location |
| ------ | ----------- | -------- | ------------- | -------- |
| switch | description | variable | cpp condition | location |
| ------ | ----------- | -------- | ------------- | -------- |
| --allow-pre-commit-input |  Allows processing of input before a frame has been committed.  TODO(crbug.com/987626): Used by headless. Look for a way not  involving a command line switch. | kAllowPreCommitInput |  | ../chromium/src/third_party/blink/common/switches.cc |
| --beforeunload-event-cancel-by-prevent-default-policy |  Used to communicate managed policy for the  BeforeunloadEventCancelByPreventDefault feature. This feature is typically  controlled by base::Feature (see blink/common/features.*) but requires an  enterprise policy override. This is implicitly a tri-state, and can be either  unset, or set to "1" for force enable, or "0" for force disable. | kBeforeunloadEventCancelByPreventDefaultPolicy |  | ../chromium/src/third_party/blink/common/switches.cc |
| --0 |  | kIntensiveWakeUpThrottlingPolicy_ForceDisable |  | ../chromium/src/third_party/blink/common/switches.cc |
| --1 |  | kIntensiveWakeUpThrottlingPolicy_ForceEnable |  | ../chromium/src/third_party/blink/common/switches.cc |
| --blink-settings |  Set blink settings. Format is <name>[=<value],<name>[=<value>],...  The names are declared in Settings.json5. For boolean type, use "true",  "false", or omit '=<value>' part to set to true. For enum type, use the int  value of the enum value. Applied after other command line flags and prefs. | kBlinkSettings |  | ../chromium/src/third_party/blink/common/switches.cc |
| --dark-mode-settings |  Sets dark mode settings. Format is [<param>=<value>],[<param>=<value>],...  The params take either int or float values. If params are not specified,  the default dark mode settings is used. Valid params are given below.  "InversionAlgorithm" takes int value of DarkModeInversionAlgorithm enum.  "ImagePolicy" takes int value of DarkModeImagePolicy enum.  "ForegroundBrightnessThreshold" takes 0 to 255 int value.  "BackgroundBrightnessThreshold" takes 0 to 255 int value.  "ContrastPercent" takes -1.0 to 1.0 float value. Higher the value, more  the contrast. | kDarkModeSettings |  | ../chromium/src/third_party/blink/common/switches.cc |
| --data-url-in-svg-use-enabled |  Overrides data: URLs in SVGUseElement deprecation through enterprise policy. | kDataUrlInSvgUseEnabled |  | ../chromium/src/third_party/blink/common/switches.cc |
| --default-tile-width |  Sets the tile size used by composited layers. | kDefaultTileWidth |  | ../chromium/src/third_party/blink/common/switches.cc |
| --default-tile-height |  | kDefaultTileHeight |  | ../chromium/src/third_party/blink/common/switches.cc |
| --force-permission-policy-unload-default-enabled |  If set, the unload event cannot be disabled by default by Permissions-Policy. | kForcePermissionPolicyUnloadDefaultEnabled |  | ../chromium/src/third_party/blink/common/switches.cc |
| --disable-image-animation-resync |  Disallow image animations to be reset to the beginning to avoid skipping  many frames. Only effective if compositor image animations are enabled. | kDisableImageAnimationResync |  | ../chromium/src/third_party/blink/common/switches.cc |
| --disable-low-res-tiling |  When using CPU rasterizing disable low resolution tiling. This uses  less power, particularly during animations, but more white may be seen  during fast scrolling especially on slower devices. | kDisableLowResTiling |  | ../chromium/src/third_party/blink/common/switches.cc |
| --disable-partial-raster |  Disable partial raster in the renderer. Disabling this switch also disables  the use of persistent gpu memory buffers. | kDisablePartialRaster |  | ../chromium/src/third_party/blink/common/switches.cc |
| --disable-prefer-compositing-to-lcd-text |  Disable the creation of compositing layers when it would prevent LCD text. | kDisablePreferCompositingToLCDText |  | ../chromium/src/third_party/blink/common/switches.cc |
| --disable-rgba-4444-textures |  Disables RGBA_4444 textures. | kDisableRGBA4444Textures |  | ../chromium/src/third_party/blink/common/switches.cc |
| --disable-zero-copy |  Disable rasterizer that writes directly to GPU memory associated with tiles. | kDisableZeroCopy |  | ../chromium/src/third_party/blink/common/switches.cc |
| --dump-blink-runtime-call-stats |  Logs Runtime Call Stats. --single-process also needs to be used along with  this for the stats to be logged. | kDumpRuntimeCallStats |  | ../chromium/src/third_party/blink/common/switches.cc |
| --enable-gpu-memory-buffer-compositor-resources |  Specify that all compositor resources should be backed by GPU memory buffers. | kEnableGpuMemoryBufferCompositorResources |  | ../chromium/src/third_party/blink/common/switches.cc |
| --enable-leak-detection-heap-snapshot |  Enables taking a heap snapshot and dumping it to file when using leak  detection. | kEnableLeakDetectionHeapSnapshot |  | ../chromium/src/third_party/blink/common/switches.cc |
| --enable-low-res-tiling |  When using CPU rasterizing generate low resolution tiling. Low res  tiles may be displayed during fast scrolls especially on slower devices. | kEnableLowResTiling |  | ../chromium/src/third_party/blink/common/switches.cc |
| --enable-prefer-compositing-to-lcd-text |  Enable the creation of compositing layers when it would prevent LCD text. | kEnablePreferCompositingToLCDText |  | ../chromium/src/third_party/blink/common/switches.cc |
| --enable-rgba-4444-textures |  Enables RGBA_4444 textures. | kEnableRGBA4444Textures |  | ../chromium/src/third_party/blink/common/switches.cc |
| --enable-raster-side-dark-mode-for-images |  Enables raster side dark mode for images. | kEnableRasterSideDarkModeForImages |  | ../chromium/src/third_party/blink/common/switches.cc |
| --enable-zero-copy |  Enable rasterizer that writes directly to GPU memory associated with tiles. | kEnableZeroCopy |  | ../chromium/src/third_party/blink/common/switches.cc |
| --gpu-rasterization-msaa-sample-count |  The number of multisample antialiasing samples for GPU rasterization.  Requires MSAA support on GPU to have an effect. 0 disables MSAA. | kGpuRasterizationMSAASampleCount |  | ../chromium/src/third_party/blink/common/switches.cc |
| --intensive-wake-up-throttling-policy |  Used to communicate managed policy for the IntensiveWakeUpThrottling feature.  This feature is typically controlled by base::Feature (see  renderer/platform/scheduler/common/features.*) but requires an enterprise  policy override. This is implicitly a tri-state, and can be either unset, or  set to "1" for force enable, or "0" for force disable. | kIntensiveWakeUpThrottlingPolicy |  | ../chromium/src/third_party/blink/common/switches.cc |
| --keyboard-focusable-scrollers-enabled |  Used to communicate managed policy for KeyboardFocusableScrollers feature.  This feature is typically controlled by a RuntimeEnabledFeature, but requires  an enterprise policy override. | kKeyboardFocusableScrollersEnabled |  | ../chromium/src/third_party/blink/common/switches.cc |
| --keyboard-focusable-scrollers-opt-out |  | kKeyboardFocusableScrollersOptOut |  | ../chromium/src/third_party/blink/common/switches.cc |
| --legacy-tech-report-policy-enabled |  A command line to indicate if there ia any legacy tech report urls being set.  If so, we will send report from blink to browser process. | kLegacyTechReportPolicyEnabled |  | ../chromium/src/third_party/blink/common/switches.cc |
| --max-untiled-layer-height |  Sets the width and height above which a composited layer will get tiled. | kMaxUntiledLayerHeight |  | ../chromium/src/third_party/blink/common/switches.cc |
| --max-untiled-layer-width |  | kMaxUntiledLayerWidth |  | ../chromium/src/third_party/blink/common/switches.cc |
| --min-height-for-gpu-raster-tile |  Sets the min tile height for GPU raster. | kMinHeightForGpuRasterTile |  | ../chromium/src/third_party/blink/common/switches.cc |
| --deprecated-mutation-events-enabled |  Used to communicate managed policy for MutationEvents feature. This feature  is typically controlled by a RuntimeEnabledFeature, but requires an  enterprise policy override. | kMutationEventsEnabled |  | ../chromium/src/third_party/blink/common/switches.cc |
| --css-custom-state-deprecated-syntax-enabled |  Used to communicate managed policy for CSSCustomStateDeprecatedSynatx. This  feature is typically controlled by a RuntimeEnabledFeature, but requires an  enterprise policy override. | kCSSCustomStateDeprecatedSyntaxEnabled |  | ../chromium/src/third_party/blink/common/switches.cc |
| --network-quiet-timeout |  Sets the timeout seconds of the network-quiet timers in IdlenessDetector.  Used by embedders who want to change the timeout time in order to run web  contents on various embedded devices and changeable network bandwidths in  different regions. For example, it's useful when using FirstMeaningfulPaint  signal to dismiss a splash screen. | kNetworkQuietTimeout |  | ../chromium/src/third_party/blink/common/switches.cc |
| --show-layout-shift-regions |  Visibly render a border around layout shift rects in the web page to help  debug and study layout shifts. | kShowLayoutShiftRegions |  | ../chromium/src/third_party/blink/common/switches.cc |
| --show-paint-rects |  Visibly render a border around paint rects in the web page to help debug  and study painting behavior. | kShowPaintRects |  | ../chromium/src/third_party/blink/common/switches.cc |
| --touch-selection-strategy |  Controls how text selection granularity changes when touch text selection  handles are dragged. Should be "character" or "direction". If not specified,  the platform default is used. | kTouchTextSelectionStrategy |  | ../chromium/src/third_party/blink/common/switches.cc |
| --character |  | kTouchTextSelectionStrategy_Character |  | ../chromium/src/third_party/blink/common/switches.cc |
| --direction |  | kTouchTextSelectionStrategy_Direction |  | ../chromium/src/third_party/blink/common/switches.cc |
| --disable-standardized-browser-zoom |  Override mechanism for preserving the old non-standard behavior of CSS zoom. | kDisableStandardizedBrowserZoom |  | ../chromium/src/third_party/blink/common/switches.cc |
| --shared-array-buffer-allowed-origins |  Comma-separated list of origins that can use SharedArrayBuffer without  enabling cross-origin isolation. | kSharedArrayBufferAllowedOrigins |  | ../chromium/src/third_party/blink/common/switches.cc |
| --conditional-focus-window-ms |  Allows overriding the conditional focus window's length. | kConditionalFocusWindowMs |  | ../chromium/src/third_party/blink/common/switches.cc |
| --js-flags |  Specifies the flags passed to JS engine. | kJavaScriptFlags |  | ../chromium/src/third_party/blink/common/switches.cc |
| switch | description | variable | cpp condition | location |
| ------ | ----------- | -------- | ------------- | -------- |
| switch | description | variable | cpp condition | location |
| ------ | ----------- | -------- | ------------- | -------- |
| switch | description | variable | cpp condition | location |
| ------ | ----------- | -------- | ------------- | -------- |
| switch | description | variable | cpp condition | location |
| ------ | ----------- | -------- | ------------- | -------- |
| switch | description | variable | cpp condition | location |
| ------ | ----------- | -------- | ------------- | -------- |
| switch | description | variable | cpp condition | location |
| ------ | ----------- | -------- | ------------- | -------- |
| switch | description | variable | cpp condition | location |
| ------ | ----------- | -------- | ------------- | -------- |
| switch | description | variable | cpp condition | location |
| ------ | ----------- | -------- | ------------- | -------- |
| switch | description | variable | cpp condition | location |
| ------ | ----------- | -------- | ------------- | -------- |
| switch | description | variable | cpp condition | location |
| ------ | ----------- | -------- | ------------- | -------- |
| switch | description | variable | cpp condition | location |
| ------ | ----------- | -------- | ------------- | -------- |
| switch | description | variable | cpp condition | location |
| ------ | ----------- | -------- | ------------- | -------- |
| switch | description | variable | cpp condition | location |
| ------ | ----------- | -------- | ------------- | -------- |
| switch | description | variable | cpp condition | location |
| ------ | ----------- | -------- | ------------- | -------- |
| switch | description | variable | cpp condition | location |
| ------ | ----------- | -------- | ------------- | -------- |
| switch | description | variable | cpp condition | location |
| ------ | ----------- | -------- | ------------- | -------- |
| switch | description | variable | cpp condition | location |
| ------ | ----------- | -------- | ------------- | -------- |
| switch | description | variable | cpp condition | location |
| ------ | ----------- | -------- | ------------- | -------- |
| switch | description | variable | cpp condition | location |
| ------ | ----------- | -------- | ------------- | -------- |
| switch | description | variable | cpp condition | location |
| ------ | ----------- | -------- | ------------- | -------- |
| switch | description | variable | cpp condition | location |
| ------ | ----------- | -------- | ------------- | -------- |
| switch | description | variable | cpp condition | location |
| ------ | ----------- | -------- | ------------- | -------- |
| switch | description | variable | cpp condition | location |
| ------ | ----------- | -------- | ------------- | -------- |
| switch | description | variable | cpp condition | location |
| ------ | ----------- | -------- | ------------- | -------- |
| switch | description | variable | cpp condition | location |
| ------ | ----------- | -------- | ------------- | -------- |
| switch | description | variable | cpp condition | location |
| ------ | ----------- | -------- | ------------- | -------- |
| switch | description | variable | cpp condition | location |
| ------ | ----------- | -------- | ------------- | -------- |
| switch | description | variable | cpp condition | location |
| ------ | ----------- | -------- | ------------- | -------- |
| switch | description | variable | cpp condition | location |
| ------ | ----------- | -------- | ------------- | -------- |
| switch | description | variable | cpp condition | location |
| ------ | ----------- | -------- | ------------- | -------- |
| switch | description | variable | cpp condition | location |
| ------ | ----------- | -------- | ------------- | -------- |
| switch | description | variable | cpp condition | location |
| ------ | ----------- | -------- | ------------- | -------- |
| switch | description | variable | cpp condition | location |
| ------ | ----------- | -------- | ------------- | -------- |
| switch | description | variable | cpp condition | location |
| ------ | ----------- | -------- | ------------- | -------- |
| switch | description | variable | cpp condition | location |
| ------ | ----------- | -------- | ------------- | -------- |
| --enable-experimental-accessibility-autoclick |  Shows additional automatic click features that haven't launched yet. | kEnableExperimentalAccessibilityAutoclick |  | ../chromium/src/ui/accessibility/accessibility_switches.cc |
| --enable-experimental-accessibility-labels-debugging |  Enables support for visually debugging the accessibility labels  feature, which provides images descriptions for screen reader users. | kEnableExperimentalAccessibilityLabelsDebugging |  | ../chromium/src/ui/accessibility/accessibility_switches.cc |
| --enable-experimental-accessibility-language-detection |  Enables language detection on in-page text content which is then exposed to  assistive technology such as screen readers. | kEnableExperimentalAccessibilityLanguageDetection |  | ../chromium/src/ui/accessibility/accessibility_switches.cc |
| --enable-experimental-accessibility-language-detection-dynamic |  Enables language detection for dynamic content which is then exposed to  assistive technology such as screen readers. | kEnableExperimentalAccessibilityLanguageDetectionDynamic |  | ../chromium/src/ui/accessibility/accessibility_switches.cc |
| --enable-experimental-accessibility-manifest-v3 |  Switches accessibility extensions to use extensions manifest v3 while the  migration is still in progress. | kEnableExperimentalAccessibilityManifestV3 |  | ../chromium/src/ui/accessibility/accessibility_switches.cc |
| --enable-experimental-accessibility-switch-access-text |  Enables in progress Switch Access features for text input. | kEnableExperimentalAccessibilitySwitchAccessText |  | ../chromium/src/ui/accessibility/accessibility_switches.cc |
| --enable-magnifier-debug-draw-rect |  Enables debug feature for drawing rectangle around magnified region, without  zooming in. | kEnableMagnifierDebugDrawRect |  | ../chromium/src/ui/accessibility/accessibility_switches.cc |
| --enable-mac-accessibility-api-migration |  Enables the switchover to the newer NSAccessibility property-based API. | kEnableMacAccessibilityAPIMigration |  | ../chromium/src/ui/accessibility/accessibility_switches.cc |
| --generate-accessibility-test-expectations |  | kGenerateAccessibilityTestExpectations |  | ../chromium/src/ui/accessibility/accessibility_switches.cc |
| --disable-renderer-accessibility |  Turns off the accessibility in the renderer. | kDisableRendererAccessibility |  | ../chromium/src/ui/accessibility/accessibility_switches.cc |
| --force-renderer-accessibility |  Force renderer accessibility to be on instead of enabling it on demand when  a screen reader is detected. The disable-renderer-accessibility switch  overrides this if present.  This switch has an optional parameter that forces an AXMode bundle. The three  available bundle settings are: 'basic', 'form-controls', and 'complete'. If  the bundle argument is invalid, then the forced AXMode will default to  'complete'. If the bundle argument is missing, then the initial AXMode will  default to complete but allow changes to the AXMode during execution. | kForceRendererAccessibility |  | ../chromium/src/ui/accessibility/accessibility_switches.cc |
| switch | description | variable | cpp condition | location |
| ------ | ----------- | -------- | ------------- | -------- |
| --disable-overscroll-edge-effect |  Disable overscroll edge effects like those found in Android views. | kDisableOverscrollEdgeEffect | BUILDFLAG(IS_ANDROID) | ../chromium/src/ui/base/ui_base_switches.cc |
| --disable-pull-to-refresh-effect |  Disable the pull-to-refresh effect when vertically overscrolling content. | kDisablePullToRefreshEffect | BUILDFLAG(IS_ANDROID) | ../chromium/src/ui/base/ui_base_switches.cc |
| --disable-modal-animations |  Disable animations for showing and hiding modal dialogs. | kDisableModalAnimations | BUILDFLAG(IS_MAC) | ../chromium/src/ui/base/ui_base_switches.cc |
| --show-mac-overlay-borders |  Show borders around CALayers corresponding to overlays and partial damage. | kShowMacOverlayBorders | BUILDFLAG(IS_MAC) | ../chromium/src/ui/base/ui_base_switches.cc |
| --enable-resources-file-sharing |  Enable resources file sharing with ash-chrome.  This flag is enabled when feature::kLacrosResourcesFileSharing is set and  ash-side operation is successfully done. | kEnableResourcesFileSharing | BUILDFLAG(IS_CHROMEOS) | ../chromium/src/ui/base/ui_base_switches.cc |
| --system-font-family |  Specifies system font family name. Improves determenism when rendering  pages in headless mode. | kSystemFontFamily | BUILDFLAG(IS_LINUX) || BUILDFLAG(IS_CHROMEOS) | ../chromium/src/ui/base/ui_base_switches.cc |
| --ui-toolkit |  Specify the toolkit used to construct the Linux GUI. | kUiToolkitFlag | BUILDFLAG(IS_LINUX) | ../chromium/src/ui/base/ui_base_switches.cc |
| --disable-gtk-ime |  Disables GTK IME integration. | kDisableGtkIme | BUILDFLAG(IS_LINUX) | ../chromium/src/ui/base/ui_base_switches.cc |
| --disable-composited-antialiasing |  Disables layer-edge anti-aliasing in the compositor. | kDisableCompositedAntialiasing |  | ../chromium/src/ui/base/ui_base_switches.cc |
| --disable-touch-drag-drop |  Disables touch event based drag and drop. | kDisableTouchDragDrop |  | ../chromium/src/ui/base/ui_base_switches.cc |
| --disallow-non-exact-resource-reuse |  Disable re-use of non-exact resources to fulfill ResourcePool requests.  Intended only for use in layout or pixel tests to reduce noise. | kDisallowNonExactResourceReuse |  | ../chromium/src/ui/base/ui_base_switches.cc |
| --drm-virtual-connector-is-external |  Treats DRM virtual connector as external to enable display mode change in VM. | kDRMVirtualConnectorIsExternal |  | ../chromium/src/ui/base/ui_base_switches.cc |
| --enable-touch-drag-drop |  Enables touch event based drag and drop. | kEnableTouchDragDrop |  | ../chromium/src/ui/base/ui_base_switches.cc |
| --force-caption-style |  Forces the caption style for WebVTT captions. | kForceCaptionStyle |  | ../chromium/src/ui/base/ui_base_switches.cc |
| --force-dark-mode |  Forces dark mode in UI for platforms that support it. | kForceDarkMode |  | ../chromium/src/ui/base/ui_base_switches.cc |
| --force-high-contrast |  Forces high-contrast mode in native UI drawing, regardless of system  settings. Note that this has limited effect on Windows: only Aura colors will  be switched to high contrast, not other system colors. | kForceHighContrast |  | ../chromium/src/ui/base/ui_base_switches.cc |
| --lang |  The language file that we want to try to open. Of the form  language[-country] where language is the 2 letter code from ISO-639.  On Linux, this flag does not work; use the LC_*/LANG environment variables  instead. | kLang |  | ../chromium/src/ui/base/ui_base_switches.cc |
| --mangle-localized-strings |  Transform localized strings to be longer, with beginning and end markers to  make truncation visually apparent. | kMangleLocalizedStrings |  | ../chromium/src/ui/base/ui_base_switches.cc |
| --show-overdraw-feedback |  Visualize overdraw by color-coding elements based on if they have other  elements drawn underneath. This is good for showing where the UI might be  doing more rendering work than necessary. The colors are hinting at the  amount of overdraw on your screen for each pixel, as follows:   True color: No overdraw.  Blue: Overdrawn once.  Green: Overdrawn twice.  Pink: Overdrawn three times.  Red: Overdrawn four or more times. | kShowOverdrawFeedback |  | ../chromium/src/ui/base/ui_base_switches.cc |
| --slow-down-compositing-scale-factor |  Re-draw everything multiple times to simulate a much slower machine.  Give a slow down factor to cause renderer to take that many times longer to  complete, such as --slow-down-compositing-scale-factor=2. | kSlowDownCompositingScaleFactor |  | ../chromium/src/ui/base/ui_base_switches.cc |
| --tint-composited-content |  Tint composited color. | kTintCompositedContent |  | ../chromium/src/ui/base/ui_base_switches.cc |
| --top-chrome-touch-ui |  Controls touch-optimized UI layout for top chrome. | kTopChromeTouchUi |  | ../chromium/src/ui/base/ui_base_switches.cc |
| --auto |  | kTopChromeTouchUiAuto |  | ../chromium/src/ui/base/ui_base_switches.cc |
| --disabled |  | kTopChromeTouchUiDisabled |  | ../chromium/src/ui/base/ui_base_switches.cc |
| --enabled |  | kTopChromeTouchUiEnabled |  | ../chromium/src/ui/base/ui_base_switches.cc |
| --ui-disable-partial-swap |  Disable partial swap which is needed for some OpenGL drivers / emulators. | kUIDisablePartialSwap |  | ../chromium/src/ui/base/ui_base_switches.cc |
| --use-system-clipboard |  Enables the ozone x11 clipboard for linux-chromeos. | kUseSystemClipboard |  | ../chromium/src/ui/base/ui_base_switches.cc |
| switch | description | variable | cpp condition | location |
| ------ | ----------- | -------- | ------------- | -------- |
| switch | description | variable | cpp condition | location |
| ------ | ----------- | -------- | ------------- | -------- |
| --enable-pixel-output-in-tests |  Forces tests to produce pixel output when they normally wouldn't. | kEnablePixelOutputInTests |  | ../chromium/src/ui/compositor/compositor_switches.cc |
| --ui-enable-rgba-4444-textures |  | kUIEnableRGBA4444Textures |  | ../chromium/src/ui/compositor/compositor_switches.cc |
| --ui-enable-zero-copy |  | kUIEnableZeroCopy |  | ../chromium/src/ui/compositor/compositor_switches.cc |
| --ui-disable-zero-copy |  | kUIDisableZeroCopy |  | ../chromium/src/ui/compositor/compositor_switches.cc |
| --ui-show-paint-rects |  | kUIShowPaintRects |  | ../chromium/src/ui/compositor/compositor_switches.cc |
| --ui-slow-animations |  | kUISlowAnimations |  | ../chromium/src/ui/compositor/compositor_switches.cc |
| --disable-vsync-for-tests |  | kDisableVsyncForTests |  | ../chromium/src/ui/compositor/compositor_switches.cc |
| switch | description | variable | cpp condition | location |
| ------ | ----------- | -------- | ------------- | -------- |
| --ash-enable-software-mirroring |  Enables software based mirroring. | kEnableSoftwareMirroring |  | ../chromium/src/ui/display/display_switches.cc |
| --ensure-forced-color-profile |  Crash the browser at startup if the display's color profile does not match  the forced color profile. This is necessary on Mac because Chrome's pixel  output is always subject to the color conversion performed by the operating  system. On all other platforms, this is a no-op. | kEnsureForcedColorProfile |  | ../chromium/src/ui/display/display_switches.cc |
| --force-color-profile |  Force all monitors to be treated as though they have the specified color  profile. Accepted values are "srgb" and "generic-rgb" (currently used by Mac  layout tests) and "color-spin-gamma24" (used by layout tests). | kForceDisplayColorProfile |  | ../chromium/src/ui/display/display_switches.cc |
| --force-raster-color-profile |  Force rastering to take place in the specified color profile. Accepted values  are the same as for the kForceDisplayColorProfile case above. | kForceRasterColorProfile |  | ../chromium/src/ui/display/display_switches.cc |
| --force-device-scale-factor |  Overrides the device scale factor for the browser UI and the contents. | kForceDeviceScaleFactor |  | ../chromium/src/ui/display/display_switches.cc |
| --ash-host-window-bounds |  Sets a window size, optional position, optional scale factor and optional  panel radii.  "1024x768" creates a window of size 1024x768.  "100+200-1024x768" positions the window at 100,200.  "1024x768*2" sets the scale factor to 2 for a high DPI display.  "1024x768~15|15|12|12" sets the radii of the panel corners as  (upper_left=15px,upper_right=15px, lower_right=12px, upper_left=12px)  "800,0+800-800x800" for two displays at 800x800 resolution.  "800,0+800-800x800,0+1600-800x800" for three displays at 800x800 resolution. | kHostWindowBounds |  | ../chromium/src/ui/display/display_switches.cc |
| --secondary-display-layout |  Specifies the layout mode and offsets for the secondary display for  testing. The format is "<t|r|b|l>,<offset>" where t=TOP, r=RIGHT,  b=BOTTOM and L=LEFT. For example, 'r,-100' means the secondary display  is positioned on the right with -100 offset. (above than primary) | kSecondaryDisplayLayout |  | ../chromium/src/ui/display/display_switches.cc |
| --screen-config |  Specifies the initial screen configuration, or state of all displays, for  FakeDisplayDelegate, see class for format details. | kScreenConfig |  | ../chromium/src/ui/display/display_switches.cc |
| --use-first-display-as-internal |  Uses the 1st display in --ash-host-window-bounds as internal display.  This is for debugging on linux desktop. | kUseFirstDisplayAsInternal |  | ../chromium/src/ui/display/display_switches.cc |
| --display-properties |  Additional display properties are provided through this switch that are  beyond what is available via EDID encoded as JSON. Please see  `https:chromium.googlesource.com/chromiumos/platform2/+/dd10a5ae3618bb9dc5fb47ac415ebef6e9a3827d/chromeos-config/README.md#displays`  for the data format. | kDisplayProperties | BUILDFLAG(IS_CHROMEOS_ASH) | ../chromium/src/ui/display/display_switches.cc |
| --ash-enable-unified-desktop |  Enables unified desktop mode. | kEnableUnifiedDesktop | BUILDFLAG(IS_CHROMEOS_ASH) | ../chromium/src/ui/display/display_switches.cc |
| switch | description | variable | cpp condition | location |
| ------ | ----------- | -------- | ------------- | -------- |
| switch | description | variable | cpp condition | location |
| ------ | ----------- | -------- | ------------- | -------- |
| --compensate-for-unstable-pinch-zoom |  Enable compensation for unstable pinch zoom. Some touch screens display  significant amount of wobble when moving a finger in a straight line. This  makes two finger scroll trigger an oscillating pinch zoom. See  crbug.com/394380 for details. | kCompensateForUnstablePinchZoom |  | ../chromium/src/ui/events/event_switches.cc |
| --touch-slop-distance |  Overrides touch slop distance for gesture detection. The touch slop distance  is the maximum distance from the starting point of a touch sequence that a  gesture can travel before it can no longer be considered a tap. Scroll  gestures can only begin after this distance has been travelled. The switch  value is a floating point number that is interpreted as a distance in pixels. | kTouchSlopDistance |  | ../chromium/src/ui/events/event_switches.cc |
| --touch-devices |  Tells chrome to interpret events from these devices as touch events. Only  available with XInput 2 (i.e. X server 1.8 or above). The id's of the  devices can be retrieved from 'xinput list'. | kTouchDevices | BUILDFLAG(IS_LINUX) || BUILDFLAG(IS_CHROMEOS) | ../chromium/src/ui/events/event_switches.cc |
| --pen-devices |  Tells chrome to interpret events from these devices as pen events. Only  available with XInput 2 (i.e. X server 1.8 or above). The id's of the  devices can be retrieved from 'xinput list'. | kPenDevices | BUILDFLAG(IS_LINUX) || BUILDFLAG(IS_CHROMEOS) | ../chromium/src/ui/events/event_switches.cc |
| --edge-touch-filtering |  Tells Chrome to do edge touch filtering. Useful for convertible tablet. | kEdgeTouchFiltering | BUILDFLAG(IS_OZONE) | ../chromium/src/ui/events/event_switches.cc |
| --disable-cancel-all-touches |  Disable CancelAllTouches() function for the implementation on cancel single  touches. | kDisableCancelAllTouches | BUILDFLAG(IS_OZONE) | ../chromium/src/ui/events/event_switches.cc |
| --enable-microphone-mute-switch-device |  Enables logic to detect microphone mute switch device state, which disables  internal audio input when toggled. | kEnableMicrophoneMuteSwitchDeviceSwitch | BUILDFLAG(IS_OZONE) | ../chromium/src/ui/events/event_switches.cc |
| switch | description | variable | cpp condition | location |
| ------ | ----------- | -------- | ------------- | -------- |
| switch | description | variable | cpp condition | location |
| ------ | ----------- | -------- | ------------- | -------- |
| switch | description | variable | cpp condition | location |
| ------ | ----------- | -------- | ------------- | -------- |
| --animation-duration-scale |  Scale factor to apply to every animation duration. Must be >= 0.0. This will  only apply to LinearAnimation and its subclasses. | kAnimationDurationScale |  | ../chromium/src/ui/gfx/switches.cc |
| --disable-font-subpixel-positioning |  Force disables font subpixel positioning. This affects the character glyph  sharpness, kerning, hinting and layout. | kDisableFontSubpixelPositioning |  | ../chromium/src/ui/gfx/switches.cc |
| --enable-native-gpu-memory-buffers |  Enable native CPU-mappable GPU memory buffer support on Linux. | kEnableNativeGpuMemoryBuffers |  | ../chromium/src/ui/gfx/switches.cc |
| --force-prefers-reduced-motion |  Forces whether the user desires reduced motion, regardless of system  settings. | kForcePrefersReducedMotion |  | ../chromium/src/ui/gfx/switches.cc |
| --force-prefers-no-reduced-motion |  Forces whether the user desires no reduced motion, regardless of system  settings. | kForcePrefersNoReducedMotion |  | ../chromium/src/ui/gfx/switches.cc |
| --headless |  Run in headless mode, i.e., without a UI or display server dependencies. | kHeadless |  | ../chromium/src/ui/gfx/switches.cc |
| --display |  Which X11 display to connect to. Emulates the GTK+ "--display=" command line  argument. In use only with Ozone/X11. | kX11Display | BUILDFLAG(IS_LINUX) || BUILDFLAG(IS_CHROMEOS) | ../chromium/src/ui/gfx/switches.cc |
| --no-xshm |  Disables MIT-SHM extension. In use only with Ozone/X11. | kNoXshm | BUILDFLAG(IS_LINUX) || BUILDFLAG(IS_CHROMEOS) | ../chromium/src/ui/gfx/switches.cc |
| switch | description | variable | cpp condition | location |
| ------ | ----------- | -------- | ------------- | -------- |
| --disable-gpu-driver-bug-workarounds |  Disable workarounds for various GPU driver bugs. | kDisableGpuDriverBugWorkarounds |  | ../chromium/src/ui/gl/gl_switches.cc |
| --disable-gpu-vsync |  Stop the GPU from synchronizing presentation with vblank. | kDisableGpuVsync |  | ../chromium/src/ui/gl/gl_switches.cc |
| --enable-gpu-service-logging |  Turns on GPU logging (debug build only). | kEnableGPUServiceLogging |  | ../chromium/src/ui/gl/gl_switches.cc |
| --enable-gpu-service-tracing |  Turns on calling TRACE for every GL call. | kEnableGPUServiceTracing |  | ../chromium/src/ui/gl/gl_switches.cc |
| --use-angle |  Select which ANGLE backend to use. Options are:   default: Attempts several ANGLE renderers until one successfully            initializes, varying ES support by platform.   d3d9: Legacy D3D9 renderer, ES2 only.   d3d11: D3D11 renderer, ES2 and ES3.   warp: D3D11 renderer using software rasterization, ES2 and ES3.   gl: Desktop GL renderer, ES2 and ES3.   gles: GLES renderer, ES2 and ES3. | kUseANGLE |  | ../chromium/src/ui/gl/gl_switches.cc |
| --use-cmd-decoder |  Use the Pass-through command decoder, skipping all validation and state  tracking. Switch lives in ui/gl because it affects the GL binding  initialization on platforms that would otherwise not default to using  EGL bindings. | kUseCmdDecoder |  | ../chromium/src/ui/gl/gl_switches.cc |
| --enable-angle-features |  ANGLE features are defined per-backend in third_party/angle/include/platform  Enables specified comma separated ANGLE features if found. | kEnableANGLEFeatures |  | ../chromium/src/ui/gl/gl_switches.cc |
| --disable-angle-features |  Disables specified comma separated ANGLE features if found. | kDisableANGLEFeatures |  | ../chromium/src/ui/gl/gl_switches.cc |
| --use-gl |  Select which implementation of GL the GPU process should use. Options are:   desktop: whatever desktop OpenGL the user has installed (Linux and Mac            default).   egl: whatever EGL / GLES2 the user has installed (Windows default - actually        ANGLE).   swiftshader: The SwiftShader software renderer. | kUseGL |  | ../chromium/src/ui/gl/gl_switches.cc |
| --gpu-no-context-lost |  Inform Chrome that a GPU context will not be lost in power saving mode,  screen saving mode, etc.  Note that this flag does not ensure that a GPU  context will never be lost in any situations, say, a GPU reset. | kGpuNoContextLost |  | ../chromium/src/ui/gl/gl_switches.cc |
| --test-gl-lib |  Flag used for Linux tests: for desktop GL bindings, try to load this GL  library first, but fall back to regular library if loading fails. | kTestGLLib |  | ../chromium/src/ui/gl/gl_switches.cc |
| --use-gpu-in-tests |  Use hardware gpu, if available, for tests. | kUseGpuInTests |  | ../chromium/src/ui/gl/gl_switches.cc |
| --enable-sgi-video-sync |  Enable use of the SGI_video_sync extension, which can have  driver/sandbox/window manager compatibility issues. | kEnableSgiVideoSync |  | ../chromium/src/ui/gl/gl_switches.cc |
| --disable-gl-drawing-for-tests |  Disables GL drawing operations which produce pixel output. With this  the GL output will not be correct but tests will run faster. | kDisableGLDrawingForTests |  | ../chromium/src/ui/gl/gl_switches.cc |
| --override-use-software-gl-for-tests |  Forces the use of software GL instead of hardware gpu for tests. | kOverrideUseSoftwareGLForTests |  | ../chromium/src/ui/gl/gl_switches.cc |
| --disable-gl-extensions |  Disables specified comma separated GL Extensions if found. | kDisableGLExtensions |  | ../chromium/src/ui/gl/gl_switches.cc |
| --enable-swap-buffers-with-bounds |  Enables SwapBuffersWithBounds if it is supported. | kEnableSwapBuffersWithBounds |  | ../chromium/src/ui/gl/gl_switches.cc |
| --enable-direct-composition-video-overlays |  Enables using DirectComposition video overlays, even if hardware overlays  aren't supported. | kEnableDirectCompositionVideoOverlays |  | ../chromium/src/ui/gl/gl_switches.cc |
| --use-adapter-luid |  Initialize the GPU process using the adapter with the specified LUID. This is  only used on Windows, as LUID is a Windows specific structure. | kUseAdapterLuid |  | ../chromium/src/ui/gl/gl_switches.cc |
| --enable-unsafe-swiftshader |  Allow usage of SwiftShader for WebGL | kEnableUnsafeSwiftShader |  | ../chromium/src/ui/gl/gl_switches.cc |
| --direct-composition-video-swap-chain-format |  Used for overriding the swap chain format for direct composition SDR video  overlays. | kDirectCompositionVideoSwapChainFormat |  | ../chromium/src/ui/gl/gl_switches.cc |
| --disable-android-native-fence-sync-for-testing |  On some Android emulators with software GL, ANGLE  is exposing the native fence sync extension but it doesn't  actually work. This switch is used to disable the Android native fence sync  during test to avoid crashes.   TODO(https:crbug.com/337886037): Remove this flag once the upstream ANGLE  is fixed. | kDisableAndroidNativeFenceSyncForTesting | BUILDFLAG(IS_ANDROID) | ../chromium/src/ui/gl/gl_switches.cc |
| switch | description | variable | cpp condition | location |
| ------ | ----------- | -------- | ------------- | -------- |
| switch | description | variable | cpp condition | location |
| ------ | ----------- | -------- | ------------- | -------- |
| --ozone-platform |  Specify ozone platform implementation to use. | kOzonePlatform |  | ../chromium/src/ui/ozone/public/ozone_switches.cc |
| --ozone-platform-hint |  Suggests the ozone platform to use (desktop Linux only).  Can be set on  chrome:flags.  See https:crbug.com/1246928. | kOzonePlatformHint |  | ../chromium/src/ui/ozone/public/ozone_switches.cc |
| --ozone-dump-file |  Specify location for image dumps. | kOzoneDumpFile |  | ../chromium/src/ui/ozone/public/ozone_switches.cc |
| --enable-wayland-ime |  Try to enable wayland input method editor. | kEnableWaylandIme |  | ../chromium/src/ui/ozone/public/ozone_switches.cc |
| --disable-wayland-ime |  Disable wayland input method editor. | kDisableWaylandIme |  | ../chromium/src/ui/ozone/public/ozone_switches.cc |
| --wayland-text-input-version |  Specify wayland text-input protocol version.  Defaults to "1" for text-input-v1. Can specify value "3" for experimental  text-input-v3 support. | kWaylandTextInputVersion |  | ../chromium/src/ui/ozone/public/ozone_switches.cc |
| --use-wayland-explicit-grab |  Use explicit grab when opening popup windows.  See https:crbug.com/1220274 | kUseWaylandExplicitGrab |  | ../chromium/src/ui/ozone/public/ozone_switches.cc |
| --disable-explicit-dma-fences |  Disable explicit DMA-fences | kDisableExplicitDmaFences |  | ../chromium/src/ui/ozone/public/ozone_switches.cc |
| --ozone-override-screen-size |  Specifies ozone screen size. | kOzoneOverrideScreenSize |  | ../chromium/src/ui/ozone/public/ozone_switches.cc |
| switch | description | variable | cpp condition | location |
| ------ | ----------- | -------- | ------------- | -------- |
| --disable-input-event-activation-protection |  Disables the disregarding of potentially unintended input events such as  button clicks that happen instantly after the button is shown. Use this for  integration tests that do automated clicks etc. | kDisableInputEventActivationProtectionForTesting |  | ../chromium/src/ui/views/views_switches.cc |
| --draw-view-bounds-rects |  Draws a semitransparent rect to indicate the bounds of each view. | kDrawViewBoundsRects |  | ../chromium/src/ui/views/views_switches.cc |
| --view-stack-traces |  Captures stack traces on View construction to provide better debug info. | kViewStackTraces |  | ../chromium/src/ui/views/views_switches.cc |
| switch | description | variable | cpp condition | location |
| ------ | ----------- | -------- | ------------- | -------- |
| --wm-window-animations-disabled |  If present animations are disabled. | kWindowAnimationsDisabled |  | ../chromium/src/ui/wm/core/wm_core_switches.cc |
