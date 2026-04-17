#!/bin/bash

source "$(dirname "${BASH_SOURCE[0]}")/../base/constants/colors.sh"

display_msg(){
    local type
    type=${2:-""}
    if [ "$type" = "info" ]; then
        echo -e "${CYAN_COLOR:-}$1${NO_COLOR:-}"
    elif [ "$type" = "danger" ]; then
        echo -e "${RED_COLOR:-}$1${NO_COLOR:-}"
    elif [ -z "$type" ]; then
        echo -e "${BLUE_COLOR:-}$1${NO_COLOR:-}"
    fi
}