#!/bin/sh
test -f AR_Intercom_3.dmg && rm AR_Intercom_3.dmg
create-dmg \
  --volname "AR_Intercom_3" \
  --volicon "resources/app_icon.icns" \
  --background "dist_resources/macOS_dmg_bg" \
  --window-pos 200 120 \
  --window-size 800 400 \
  --icon "AR Intercom.app" 200 190 \
  --icon-size 100 \
  --hide-extension "AR Intercom.app" \
  --app-drop-link 600 185 \

  "AR_Intercom_3.dmg" \
  "source_folder"
