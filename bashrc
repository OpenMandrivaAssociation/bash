# /etc/bashrc

# System wide functions and aliases
# Environment stuff goes in /etc/profile
#
# Put local overrides in ~/.bashrc or /etc/profile.d/*.sh rather than editing
# this file directly so package updates apply cleanly.

# Set umask even for non-interactive shells.
if [ "$(id -gn)" = "$(id -un)" ] && [ "$(id -u)" -gt 99 ]; then
    umask 002
else
    umask 022
fi

# Only configure interactive bash sessions.
case $- in
    *i*) ;;
    *) return 0 ;;
esac
[ -n "${BASH_VERSION:-}" ] || return 0

# Non-login shells load /etc/profile.d/*.sh before prompt initialization so
# login and non-login shells see identical ordering and environment.
if [ -z "${loginsh:-}" ]; then
    for i in /etc/profile.d/*.sh; do
        [ -r "$i" ] && . "$i"
    done
    unset i
fi
unset loginsh

# History configuration (preserve mc's ignorespace if already set).
export HISTSIZE=
export HISTFILESIZE=
export HISTTIMEFORMAT="${HISTTIMEFORMAT:-[%F %T] }"
case ":${HISTCONTROL:-}:" in
    *:ignorespace:*) ;;
    *) export HISTCONTROL="ignoreboth:erasedups" ;;
esac

shopt -s histappend checkwinsize no_empty_cmd_completion checkhash cmdhist 2>/dev/null || :

__om_register_prompt_command() {
    local fn="$1" elem
    if ! declare -p PROMPT_COMMAND 2>/dev/null | grep -q '^declare -a '; then
        if [ -n "${PROMPT_COMMAND:-}" ]; then
            PROMPT_COMMAND=("$PROMPT_COMMAND")
        else
            PROMPT_COMMAND=()
        fi
    fi
    for elem in "${PROMPT_COMMAND[@]}"; do
        [ "$elem" = "$fn" ] && return 0
    done
    if [ "${#PROMPT_COMMAND[@]}" -gt 0 ] && [ -z "${PROMPT_COMMAND[0]:-}" ]; then
        PROMPT_COMMAND[0]="$fn"
    else
        PROMPT_COMMAND=("$fn" "${PROMPT_COMMAND[@]}")
    fi
}

__om_git_info() {
    _OM_GIT_BRANCH=""
    _OM_GIT_STATE=""
    [ "${OM_PROMPT_GIT:-1}" != "0" ] || return 0

    local dir="$PWD"
    while [ -n "$dir" ]; do
        [ -e "$dir/.git" ] && break
        dir=${dir%/*}
    done
    local git_entry="${dir:-/}/.git"
    [ -e "$git_entry" ] || return 0
    command -v git >/dev/null 2>&1 || return 0

    local git_out
    git_out=$(GIT_OPTIONAL_LOCKS=0 git status --porcelain=v2 --branch 2>/dev/null) || return 0

    local line branch="" head_oid="" ahead=0 behind=0
    local staged=0 unstaged=0 untracked=0 unmerged=0
    while IFS= read -r line; do
        case "$line" in
            "# branch.head "*) branch=${line#\# branch.head } ;;
            "# branch.oid "*)  head_oid=${line#\# branch.oid } ;;
            "# branch.ab "*)
                local ab=${line#\# branch.ab }
                ahead=${ab%% *}
                ahead=${ahead#+}
                behind=${ab##* }
                behind=${behind#-}
                ;;
            1\ *|2\ *)
                local xy=${line#? }
                xy=${xy%% *}
                case "$xy" in
                    .?*) ;;
                    *) staged=1 ;;
                esac
                case "$xy" in
                    ?.?*) ;;
                    *) unstaged=1 ;;
                esac
                ;;
            u\ *) unmerged=1 ;;
            \?\ *) untracked=1 ;;
        esac
    done <<EOF
$git_out
EOF

    if [ "$branch" = "(detached)" ]; then
        branch="@${head_oid:0:7}"
    fi
    [ -n "$branch" ] || return 0

    local gitdir=""
    if [ -d "$git_entry" ]; then
        gitdir="$git_entry"
    elif [ -f "$git_entry" ]; then
        IFS= read -r gitdir < "$git_entry" 2>/dev/null || gitdir=""
        case "$gitdir" in
            gitdir:\ *)
                gitdir=${gitdir#gitdir: }
                case "$gitdir" in
                    /*) ;;
                    *) gitdir="${dir:-/}/$gitdir" ;;
                esac
                ;;
            *) gitdir="" ;;
        esac
    fi

    local action=""
    if [ -n "$gitdir" ]; then
        if [ -d "$gitdir/rebase-merge" ] || [ -d "$gitdir/rebase-apply" ]; then
            action="REBASE"
        elif [ -f "$gitdir/MERGE_HEAD" ]; then
            action="MERGE"
        elif [ -f "$gitdir/CHERRY_PICK_HEAD" ]; then
            action="CHERRY-PICK"
        elif [ -f "$gitdir/REVERT_HEAD" ]; then
            action="REVERT"
        elif [ -f "$gitdir/BISECT_LOG" ]; then
            action="BISECT"
        fi
    fi

    local flags=""
    [ "$unmerged" -eq 1 ] && flags="${flags}!"
    [ "$staged" -eq 1 ] && flags="${flags}+"
    [ "$unstaged" -eq 1 ] && flags="${flags}*"
    [ "$untracked" -eq 1 ] && flags="${flags}?"
    if [ "$ahead" -gt 0 ]; then
        flags="${flags}${_OM_SYM_UP}${ahead}"
    fi
    if [ "$behind" -gt 0 ]; then
        flags="${flags}${_OM_SYM_DN}${behind}"
    fi

    _OM_GIT_BRANCH="$branch"
    _OM_GIT_STATE="${action:+ ($action)}${flags:+ $flags}"
}

__om_build_ps1() {
    local rc="$1"
    local style="${OM_PROMPT_STYLE:-two-line}"
    local c_frame='\[\e[90m\]'
    local c_host='\[\e[1;34m\]'
    local c_dir='\[\e[1;36m\]'
    local c_ro='\[\e[1;31m\]'
    local c_branch='\[\e[1;35m\]'
    local c_dirty='\[\e[1;33m\]'
    local c_venv='\[\e[36m\]'
    local c_err='\[\e[1;31m\]'
    local c_ok='\[\e[1;32m\]'
    local c_rst='\[\e[0m\]'

    local c_user="$c_ok"
    local c_sigil="$c_ok"
    if [ "${EUID:-$(id -u)}" -eq 0 ]; then
        c_user="$c_err"
        c_sigil="$c_err"
    elif [ "$rc" -ne 0 ]; then
        c_sigil="$c_err"
    fi

    local ro_seg=""
    [ -w "$PWD" ] || ro_seg="${c_ro} ro"

    local git_seg=""
    if [ -n "${_OM_GIT_BRANCH:-}" ]; then
        git_seg=" ${c_branch}${_OM_GIT_BRANCH}"
        [ -n "${_OM_GIT_STATE:-}" ] && git_seg="${git_seg}${c_dirty}${_OM_GIT_STATE}"
    fi

    local venv_name="" venv_seg=""
    if [ -n "${VIRTUAL_ENV:-}" ]; then
        venv_name=${VIRTUAL_ENV##*/}
        if [ "$venv_name" = ".venv" ] || [ "$venv_name" = "venv" ]; then
            local _vparent=${VIRTUAL_ENV%/*}
            venv_name="${_vparent##*/}:${venv_name}"
        fi
        venv_seg=" ${c_venv}(${venv_name})"
    elif [ -n "${CONDA_DEFAULT_ENV:-}" ]; then
        venv_seg=" ${c_venv}(${CONDA_DEFAULT_ENV})"
    fi

    local _j='\j'
    _j="${_j@P}"
    local jobs_seg=""
    [ "${_j:-0}" -gt 0 ] && jobs_seg=" ${c_dirty}${_OM_SYM_JOB}${_j}"

    local err_seg=""
    [ "$rc" -ne 0 ] && err_seg=" ${c_err}${_OM_SYM_ERR} ${rc}"

    local osc_a="" osc_b=""
    if [ "${_OM_OSC133:-0}" -eq 1 ]; then
        osc_a='\[\e]133;A\a\]'
        osc_b='\[\e]133;B\a\]'
    fi

    case "$style" in
        plain|off)
            PS1="${osc_a}[\u@\h \W]\\\$ ${osc_b}"
            ;;
        single|compact)
            PS1="${osc_a}${c_frame}(${c_user}\u${c_frame}@${c_host}\h${c_frame})-[${c_dir}\w${ro_seg}${git_seg}${c_frame}]${venv_seg}${jobs_seg}${err_seg} ${c_sigil}\\\$${c_rst} ${osc_b}"
            ;;
        *)
            PS1="${osc_a}${c_frame}${_OM_BOX_TL}(${c_user}\u${c_frame}@${c_host}\h${c_frame})${_OM_BOX_H}[${c_dir}\w${ro_seg}${git_seg}${c_frame}]${venv_seg}\n${c_frame}${_OM_BOX_BL}${err_seg}${jobs_seg} ${c_sigil}\\\$${c_rst} ${osc_b}"
            ;;
    esac
    __OM_MANAGED_PS1="$PS1"
}

__om_prompt_precmd() {
    local rc=$?
    if [ -n "${STARSHIP_SHELL:-}" ] && [ -n "${STARSHIP_CMD_STATUS:-}" ]; then
        rc="$STARSHIP_CMD_STATUS"
    fi

    # Flush completed command to shared history immediately.
    history -a

    # Emit semantic completion (OSC 133;D + 133;L) when pure-Bash prompt owns 133;A/B.
    if [ "${_OM_OSC133:-0}" -eq 1 ] && [ "${__OM_PROMPT_SHOWN:-0}" -eq 1 ] && \
       [ -n "${__OM_MANAGED_PS1:-}" ] && [ "${PS1:-}" = "${__OM_MANAGED_PS1}" ]; then
        printf '\033]133;D;%d\007\033]133;L\007' "$rc"
    fi
    __OM_PROMPT_SHOWN=1

    # Update terminal window/tab title without overwriting PROMPT_COMMAND.
    if [ "${_OM_HAS_TITLE:-0}" -eq 1 ]; then
        local title_pwd="$PWD"
        if [ -n "${HOME:-}" ] && [ "$HOME" != "/" ]; then
            case "$PWD" in
                "$HOME")   title_pwd="~" ;;
                "$HOME"/*) title_pwd="~/${PWD#"$HOME"/}" ;;
            esac
        fi
        if [ "${TERM:-}" = "screen" ]; then
            printf '\033_%s@%s:%s\033\\' "${USER:-}" "${HOSTNAME%%.*}" "$title_pwd"
        else
            printf '\033]0;%s@%s:%s\007' "${USER:-}" "${HOSTNAME%%.*}" "$title_pwd"
        fi
    fi

    # Respect user-customized PS1 (or external prompt engines like Starship).
    if [ -n "${__OM_MANAGED_PS1:-}" ] && [ "${PS1:-}" = "${__OM_MANAGED_PS1}" ]; then
        __om_git_info
        __om_build_ps1 "$rc"
    fi

    return "$rc"
}

if [ -z "${__OM_BASHRC_INITIALIZED:-}" ]; then
    __OM_BASHRC_INITIALIZED=1

    # Keep paths readable without shrinking directory context too aggressively.
    : "${PROMPT_DIRTRIM:=3}"

    if [ "${TERM:-dumb}" = "dumb" ] || [ "${OM_PROMPT_STYLE:-two-line}" = "off" ]; then
        [ "$PS1" = '\s-\v\$ ' ] && PS1='[\u@\h \W]\$ '
    else
        case "${LC_ALL:-${LC_CTYPE:-${LANG:-}}}" in
            *[Uu][Tt][Ff]-*8*|*[Uu][Tt][Ff]8*)
                _OM_IS_UTF8=1
                _OM_BOX_TL="┌──"
                _OM_BOX_H="─"
                _OM_BOX_BL="└─"
                _OM_SYM_ERR="×"
                _OM_SYM_UP="↑"
                _OM_SYM_DN="↓"
                _OM_SYM_JOB="•"
                ;;
            *)
                _OM_IS_UTF8=0
                _OM_BOX_TL="+--"
                _OM_BOX_H="-"
                _OM_BOX_BL="|-"
                _OM_SYM_ERR="x"
                _OM_SYM_UP="+"
                _OM_SYM_DN="-"
                _OM_SYM_JOB="*"
                ;;
        esac

        case "${TERM:-}" in
            xterm*|konsole*|screen*|tmux*|rxvt*|alacritty*|foot*|wezterm*|kitty*)
                _OM_HAS_TITLE=1
                _OM_OSC133=1
                ;;
            *)
                _OM_HAS_TITLE=0
                _OM_OSC133=0
                ;;
        esac

        # Enable Starship in capable UTF-8 terminals when configured (or opt-in via
        # OM_USE_STARSHIP=1), falling back to the pure-Bash prompt otherwise.
        _om_use_starship=0
        if [ "${OM_USE_STARSHIP:-1}" = "1" ] && [ "${_OM_IS_UTF8:-0}" -eq 1 ] && \
           [ "${_OM_HAS_TITLE:-0}" -eq 1 ] && command -v starship >/dev/null 2>&1 && \
           ( [ "$PS1" = '\s-\v\$ ' ] || [ "$PS1" = '[\u@\h \W]\$ ' ] || [ "$PS1" = '\$ ' ] ); then
            if [ -n "${STARSHIP_CONFIG:-}" ] || [ -e "${XDG_CONFIG_HOME:-$HOME/.config}/starship.toml" ]; then
                _om_use_starship=1
            elif [ -r /etc/starship.toml ]; then
                export STARSHIP_CONFIG=/etc/starship.toml
                _om_use_starship=1
            elif [ "${OM_USE_STARSHIP:-0}" = "1" ]; then
                _om_use_starship=1
            fi
        fi

        if [ "$_om_use_starship" -eq 1 ]; then
            declare -a _om_saved_pc=()
            if declare -p PROMPT_COMMAND 2>/dev/null | grep -q '^declare -a '; then
                _om_saved_pc=("${PROMPT_COMMAND[@]}")
            elif [ -n "${PROMPT_COMMAND:-}" ]; then
                _om_saved_pc=("$PROMPT_COMMAND")
            fi
            PROMPT_COMMAND=()
            eval "$(starship init bash)"
            PROMPT_COMMAND=()
            __om_register_prompt_command "starship_precmd"
            PROMPT_COMMAND+=("__om_prompt_precmd" "${_om_saved_pc[@]}")
            unset _om_saved_pc _om_use_starship
        else
            if [ "${_OM_OSC133:-0}" -eq 1 ]; then
                case "${PS0:-}" in
                    *'133;C'*) ;;
                    *) PS0="${PS0:-}"'\e]133;C\a' ;;
                esac
            fi
            if [ "$PS1" = '\s-\v\$ ' ] || [ "$PS1" = '[\u@\h \W]\$ ' ] || [ "$PS1" = '\$ ' ]; then
                __om_git_info
                __om_build_ps1 0
            fi
            __om_register_prompt_command "__om_prompt_precmd"
            unset _om_use_starship
        fi
    fi

    if ! declare -p PROMPT_COMMAND 2>/dev/null | grep -q "__om_prompt_precmd"; then
        __om_register_prompt_command "__om_prompt_precmd"
    fi
fi
