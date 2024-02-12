#!/usr/bin/env bash
{% include 'misc/header.py' %}

# Quit on errors
set -o errexit

# Quit on unbound symbols
set -o nounset

# COLORS for messages
NC='\033[0m'                    # Default color
INFO_COLOR='\033[1;97;44m'      # Bold + white + blue background
SUCCESS_COLOR='\033[1;97;42m'   # Bold + white + green background
ERROR_COLOR='\033[1;97;41m'     # Bold + white + red background

PROGRAM=`basename $0`
SCRIPT_PATH=$(dirname "$0")

# MESSAGES
msg() {
  echo -e "${1}" 1>&2
}
# Display a colored message
# More info: https://misc.flogisoft.com/bash/tip_colors_and_formatting
# $1: choosen color
# $2: title
# $3: the message
colored_msg() {
  msg "${1}[${2}]: ${3}${NC}"
}

info_msg() {
  colored_msg "${INFO_COLOR}" "INFO" "${1}"
}

error_msg() {
  colored_msg "${ERROR_COLOR}" "ERROR" "${1}"
}

error_msg+exit() {
    error_msg "${1}" && exit 1
}

success_msg() {
  colored_msg "${SUCCESS_COLOR}" "SUCCESS" "${1}"
}

success_msg+exit() {
  colored_msg "${SUCCESS_COLOR}" "SUCCESS" "${1}" && exit 0
}

# Displays program name
msg "PROGRAM: ${PROGRAM}"

# Poetry is a mandatory condition to launch this program!
if [[ -z "${VIRTUAL_ENV}" ]]; then
  error_msg+exit "Error - Launch this script via poetry command:\n\tpoetry run ${PROGRAM}"
fi

info_msg "Test pydocstyle:"
pydocstyle inv_test tests docs
info_msg "Test isort:"
isort --check-only --diff tests {{ cookiecutter.package_name }}
info_msg "Test useless imports:"
autoflake -c -r --remove-all-unused-imports --ignore-init-module-imports . &> /dev/null || {
  autoflake --remove-all-unused-imports -r --ignore-init-module-imports .
  exit 1
}

info_msg "Sphinx-build:"
sphinx-build -qnNW docs docs/_build/html

success_msg+exit "Perfect ${PROGRAM} external! See you soon…"
