# pulsar-pkgs

Custom package repository for Pulsar ISO builds.

## Packages

| Package | Description | Source Branch |
|---------|-------------|---------------|
| `cnchi` | Pulsar graphical installer | `0.16.x` (stable), `cnchi-dev` (development) |
| `pulsar-keyring` | GPG keyring for the repo |
| `pulsar-mirrorlist` | Mirror list for `[pulsar-pkgs]` |
| `pulsar-desktop-settings` | Custom GTK/Plasma theme, dconf defaults |
| `pulsar-wallpapers` | Pulsar desktop wallpapers |
| `yay` | AUR helper |
| `downgrade` | Pacman package downgrade tool |

## Usage

Add to `/etc/pacman.conf`:

```
[pulsar-pkgs]
SigLevel = Optional TrustAll
Server = https://Pulsar-OS.github.io/pulsar-pkgs/
```

Then:

```
pacman -Sy
pacman -S cnchi pulsar-desktop-settings
```

## Branches

- `main` — package definitions, CI generates the repo
- Cnchi sources shipped from `Pulsar-OS/Cnchi` (`0.16.x` and `cnchi-dev` branches)

## License

GPL-2.0
