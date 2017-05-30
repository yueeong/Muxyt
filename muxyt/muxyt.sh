#!/usr/bin/env bash

while getopts ":j:" opt; do
  case $opt in
    j)
      echo "-js was triggered!" >&2
      ;;
    \?)
      echo "Invalid option: -$OPTARG" >&2
      ;;
  esac
done