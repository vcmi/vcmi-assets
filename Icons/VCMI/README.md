# VCMI Icon

## Workflow
The icon is based on an image created using the Stable Diffusion model available under https://text2img.org/, which has been trained using the LAION-5B data set and which is free to use.

The following prompt was used:

```
game icon showing a medieval shield, azure blue medieval heater shield showing a golden heraldic lion with a silver border with rivets, white background, trending on ArtStation, simple background, 3d render, icon for a fantasy game
```

The resulting image has then been upscaled and edited using GIMP and Inkscape. To ensure that the brown and white quadrants are aligned to the pixel grid, the quadrants have been selected using the 16px version of the icon.

To ensure that the VCMI text is aligned to the pixel grid, separate .svg files have been created for various resolutions.

The .ico file has been created in GIMP by opening the various icon sizes as layers and exporting the file.

The .icns file has been created using [icnsutil](https://pypi.org/project/icnsutil/) and can be previewed using the [icnsutil viewer](https://relikd.github.io/icnsutil/html/viewer.html)

```
icnsutil c -f vcmi.icns vcmiclient.16x16.png vcmiclient.32x32.png vcmiclient.48x48.png vcmiclient.128x128.png vcmiclient.256x256.png vcmiclient.512x512.png vcmiclient.1024x1024.png --toc
```

## List of icon assets used by VCMI
* android/vcmi-app/src/main/res/mipmap-{m,h,xh,xxh,xxxh}dpi/ic_launcher.png
* client/icons/vcmiclient.{res}x{res}.png
* client/icons/vcmiclient.svg
* client/ios/Images.xcassets/AppIcon.appiconset/Icon-App-{res}x{res}@{scale_factor}x.png
* client/ios/vcmi_logo.png
* client/vcmi.ico
* launcher/icons/menu-game.png
* launcher/VCMI_launcher.ico
* mapeditor/icons/menu-game.png
* Mods/vcmi/Sprites/mapFormatIcons/vcmi1.png
* osx/vcmi.icns