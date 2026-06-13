#!/bin/bash
set -e

echo "Setting up Pulsar PKGS..."

if [[ $EUID -ne 0 ]]; then
   echo "Run with sudo!"
   exit 1
fi

cp /etc/pacman.conf /etc/pacman.conf.backup

if ! grep -q "\[pulsar-pkgs\]" /etc/pacman.conf; then
    cat >> /etc/pacman.conf << 'CONF'

[pulsar-pkgs]
SigLevel = Optional TrustAll
Server = https://Pulsar-Linux.github.io/pulsar-pkgs/
CONF
    echo "Added pulsar-pkgs to pacman.conf"
else
    echo "pulsar-pkgs already in pacman.conf"
fi

pacman -Sy

echo "Pulsar PKGS ready!"
