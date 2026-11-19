#!/bin/sh
# Linux-Mandrake / OpenMandriva common interactive shell aliases.
#
# If ~/.alias exists and LOAD_SYSTEM_ALIASES is unset, skip system aliases.
# If IGNORE_SYSTEM_ALIASES is non-empty, skip system aliases.

case $- in
    *i*) ;;
    *) return 0 ;;
esac

# Don't define aliases in plain Bourne shell.
[ -n "${BASH_VERSION:-}${KSH_VERSION:-}${ZSH_VERSION:-}" ] || return 0

[ -f "$HOME/.alias" ] && [ -z "${LOAD_SYSTEM_ALIASES:-}" ] && return 0
[ -n "${IGNORE_SYSTEM_ALIASES:-}" ] && return 0

if [ -z "${LS_COLORS:-}" ] && command -v dircolors >/dev/null 2>&1; then
    if [ -f "$HOME/.dir_colors" ]; then
        eval "$(dircolors --sh "$HOME/.dir_colors")"
    elif [ -f /etc/DIR_COLORS ]; then
        eval "$(dircolors --sh /etc/DIR_COLORS)"
    fi
fi

# Note: do not add custom aliases here as this file is managed by the bash package;
# put custom overrides in ~/.bashrc or a separate /etc/profile.d/*.sh file.

LS_OPTIONS="-F"
if [ "${TERM:-dumb}" != "emacs" ] && [ "${TERM:-dumb}" != "dumb" ]; then
    LS_OPTIONS="$LS_OPTIONS --color=auto"
fi

alias ls="ls $LS_OPTIONS"
alias d="ls"
alias l="ls"
alias ll="ls -lh"
alias la="ls -la"
alias lsd="ls -d */"
alias cd..="cd .."
alias s="cd .."
alias p="cd -"

alias md="mkdir"
alias rd="rmdir"
alias cp="cp -i"
alias mv="mv -i"
alias rm="rm -i"

# Colored grep without triggering obsolescent egrep/fgrep warnings
if [ "${TERM:-dumb}" != "dumb" ]; then
    alias grep="grep --color=auto"
    alias egrep="grep -E --color=auto"
    alias fgrep="grep -F --color=auto"
    alias dmesg="dmesg --ctime --color=auto"
else
    alias egrep="grep -E"
    alias fgrep="grep -F"
fi

# Human-readable sizes and progress by default
alias du='du -h'
alias dd='dd status=progress'
alias df='df -h -x supermount'
