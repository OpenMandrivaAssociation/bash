#!/bin/sh
# Linux-Mandrake configuration: Chmouel Boudjnah <chmouel@mandrakesoft.com>
#
# Common Aliases for a system.
#
# The Semantic is :
#	If exist a ~/.alias and the user hasn't specified a
#	LOAD_SYSTEM_ALIAS variables then don't do any system aliases
#	If there is no ~/.alias but the user has specified a
#	IGNORE_SYSTEM_ALIASES then don't do any system aliases.

[ -f ~/.alias ] && [ -z $LOAD_SYSTEM_ALIASES ] && return 0
[ -n "$IGNORE_SYSTEM_ALIASES" ] && return 0

if [ -f ~/.dir_colors ]; then
    eval $(dircolors --sh ~/.dir_colors)
else
    eval $(dircolors --sh /etc/DIR_COLORS)
fi

# Don't define aliases in plain Bourne shell
[ -n "${BASH_VERSION}${KSH_VERSION}${ZSH_VERSION}" ] || return 0

# default ls options
LS_OPTIONS="-F"

# emacs doesn't support color
if [ $TERM != "emacs" ];then
    LS_OPTIONS="$LS_OPTIONS --color=auto"
fi

# Note that you should not add custom aliases here as this file will be
# overwritten when package bash is upgraded. Instead create an own profile
# file for any added aliases.

alias ls="ls $LS_OPTIONS"

alias d="ls"
alias l="ls"			# classical listing.
alias ll="ls -l"		# List detailled.
alias la='ls -a'		# List all.
alias lsd="ls -d */"		# List only the directory.
alias cd..="cd .."
alias s="cd .."
alias p="cd -"

alias md="mkdir"
alias rd="rmdir"
alias cp="cp -i"
alias mv="mv -i"
alias rm="rm -i"

# colored grep by default
alias grep="grep --color"
# colored grep by default
alias egrep="egrep --color"
# colored grep by default
alias fgrep="fgrep --color"
# colored dmesg with human-readable timestamps by default
alias dmesg="dmesg --ctime --color"

# Size of a directory (by default Human Readable).
alias du='du -h'
alias dd='dd status=progress'

# Size of a disk (by default Human Readable).
# and don't probe supermount
alias df='df -h -x supermount'
