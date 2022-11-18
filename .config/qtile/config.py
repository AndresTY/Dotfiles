from typing import List  # noqa: F401

from libqtile import bar, layout, widget, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
import subprocess
from os import path
mod = "mod4"
terminal = guess_terminal()

# ---------------Keys-------------
keys = [
    # Move between windons
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    # Change window sizes
    Key([mod, "shift"], "l", lazy.layout.grow(), desc="grow window"),
    Key([mod, "shift"], "h", lazy.layout.shrink(), desc="shrink window"),
    Key([mod], "a", lazy.window.toggle_floating()),

    # Toggle between different layout as define below
    Key([mod], "Tab", lazy.next_layout()),
    Key([mod, "shift"], "Tab", lazy.prev_layout()),

    # Window administration
    Key([mod], "w", lazy.window.kill()),
    Key([mod, "control"], "period", lazy.layout.next()),
    Key([mod, "shift"], "period", lazy.screen.next_group()),
    Key([mod, "shift"], "comma", lazy.screen.prev_group()),
    Key([mod], "period", lazy.group.next_window()),
    Key([mod], "comma", lazy.group.prev_window()),
    Key([mod, "control"], "r", lazy.restart()),
    Key([mod, "control"], "q", lazy.shutdown()),
    Key([mod], "r", lazy.spawncmd()),

    # APPS
    Key([mod], "m", lazy.spawn("rofi -show combi"), desc="MENU"),
    Key([mod, "shift"], "e", lazy.spawn(
        "rofi -show filebrowser -i"), desc="MENU"),
    Key([mod, "shift"], "m", lazy.spawn("rofi -show"), desc="open apps MENU"),
    Key([mod], "b", lazy.spawn("firefox"), desc="firefox like browser"),
    Key([mod, "shift"], "b", lazy.spawn(
        "chromium"), desc="chromium like browser"),
    Key([mod], "e", lazy.spawn("Thunar"), desc="file manager"),
    Key([mod], "Return", lazy.spawn("alacritty"), "terminal"),
    Key([mod], "r", lazy.spawn("redshift -O 2400")),
    Key([mod, "shift"], "r", lazy.spawn("redshift -x")),
    Key([mod], "s", lazy.spawn("flameshot")),

    # ------------ Hardware Configs ------------
    Key([], "XF86AudioLowerVolume", lazy.spawn(
        "pactl set-sink-volume @DEFAULT_SINK@ -5%"
    ), desc="down volumen"),
    Key([], "XF86AudioRaiseVolume", lazy.spawn(
        "pactl set-sink-volume @DEFAULT_SINK@ +5%"
    ), desc="up volumen"),
    Key([], "XF86AudioMute", lazy.spawn(
        "pactl set-sink-mute @DEFAULT_SINK@ toggle"
    ), desc="Mute volumen"),
    Key([], "XF86MonBrightnessUp", lazy.spawn(
        "brightnessctl set +10%"), desc="up brightness"),
    Key([], "XF86MonBrightnessDown", lazy.spawn(
        "brightnessctl set 10%-"), desc="brightness"),
]

# ----------groups---------
groups = [Group(i) for i in [
    "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ",
]]

for i, group in enumerate(groups):
    actual_key = str(i + 1)
    keys.extend([
        # Switch to workspace N
        Key([mod], actual_key, lazy.group[group.name].toscreen()),
        # Send window to workspace N
        Key([mod, "shift"], actual_key, lazy.window.togroup(group.name))
    ])

# -----------Layout----------
layouts = [
    layout.Max(),
    layout.Zoomy(),
    layout.Columns(border_focus='6e0cad', border_focus_stack='6e0cad',
                   border_normal='000000', border_normal_stack='000000'),
    #layout.Stack(num_stacks=2, border_focus='6e0cad', border_normal='000000'),
    #layout.Bsp(border_focus='6e0cad', border_normal='000000'),
    #layout.Matrix(border_focus='6e0cad', border_normal='000000'),
    #layout.MonadTall(border_focus='6e0cad', border_normal='000000'),
    #layout.MonadWide(border_focus='6e0cad', border_normal='000000'),
    #layout.RatioTile(border_focus='6e0cad', border_normal='000000'),
    #layout.Tile(border_focus='6e0cad', border_normal='000000'),
    #layout.VerticalTile(border_focus='6e0cad', border_normal='000000'),
    #layout.TreeTab(bg_color='000000', active_bg='6e0cad', active_fg='000000',inactive_bg='000000', inactive_fg='6e0cad', sections=[' ']),
]
# ----------Widgets------------

base = lambda fg="#ffffff", bg="#000000": {
    'foreground': fg,
    'background': bg
}


def separator(line=0): return widget.Sep(**base(), linewidth=line, padding=5)


icon = lambda fg="#ffffff", bg="#000000", fontsize=16, text="?": widget.TextBox(
    **base(fg, bg),
    fontsize=fontsize,
    text=text,
    padding=3
)

powerline = lambda fg="#6e0cad", bg="#000000": widget.TextBox(
    **base(fg, bg),
    text="|",
    fontsize=20,
    padding=5
)


def workspaces(): return [
    separator(),
    widget.GroupBox(
        **base(),
        font='UbuntuMono Nerd Font',
        fontsize=17,
        margin_y=3,
        margin_x=0,
        padding_y=8,
        padding_x=5,
        borderwidth=1,
        active='#cc9df9',
        inactive='#000000',
        rounded=True,
        highlight_method='line',
        highlight_color = ['cc9df9','000000'],
        urgent_alert_method='line',
        urgent_border='ffffff',
        this_current_screen_border="#130317",
        this_screen_border='#130317',
        other_current_screen_border='#ffffff',
        other_screen_border='#ffffff',
        disable_drag=True
    ),
    separator(),
    widget.Spacer(**base(), length=170),
    widget.Clock( format='%d/%m/%Y - %H:%M '),
    separator(),
    widget.Spacer(**base()),
]


primary_widgets = [
    *workspaces(),

    separator(),


    widget.CPUGraph(border_color='822323',graph_color='eb1818',fill_color='eb1616.5'),
    # #powerline'#370656 '#000000'),

    #icon(text=' '),  # Icon: nf-fa-feed

    # interface='wlan0'

    #widget.Net(format='{total}'),
    widget.Wlan(format='{essid}', foreground='18BAEB'),
    widget.NetGraph(linewidth=1),
    separator(),

    widget.MemoryGraph(border_color='238229',graph_color='18eb1c',fill_color='18eb1c.5'),
    # #powerline'#400879', '#420767'),

    #widget.CurrentLayoutIcon(scale=0.65),

    #widget.CurrentLayout(padding=5),
    #separator(),

    # powerline'#58098A', '#400879'),

    # powerline('#630A9B', '#58098A'),

    # icon(bg="#630A9B", text=' '),  # Icon: nf-fa-download

    widget.Battery( show_short_text=False, charge_char=' ', discharge_char=' ', empty_char=' ', full_char=' ',
                   format='{percent:2.0%} {char}', low_percentage=0.2, update_interval=10),

    separator(),
    # powerline('#6e0cad', '#630A9B'),

    widget.Systray(background='2e2e2e',padding=5),

]

secondary_widgets = [
    *workspaces(),

    separator(),

    # powerline('#130317', '#6e0cad'),

    widget.CurrentLayoutIcon(**base(bg='#130317'), scale=0.65),

    widget.CurrentLayout(**base(bg='#130317'), padding=5),
]

widget_defaults = {
    'font': 'UbuntuMono Nerd Font Bold',
    'fontsize': 12,
    'padding': 1,
}
extension_defaults = widget_defaults.copy()

# ----------SCREENS------


def status_bar(widgets): return bar.Bar(
    widgets,
    20,
    opacity=0.5,
    background='#000000',
    foreground='#ffffff')


screens = [Screen(top=status_bar(primary_widgets))]

connected_monitors = subprocess.run(
    "xrandr | grep 'connected' | cut -d ' ' -f 2",
    shell=True,
    stdout=subprocess.PIPE
).stdout.decode("UTF-8").split("\n")[:-1].count("connected")

if connected_monitors > 1:
    for i in range(1, connected_monitors):
        screens.append(Screen(top=status_bar(secondary_widgets)))
"""

screens = [
    Screen(
        bottom=bar.Bar(
            [
                widget.CurrentLayout(),
                widget.GroupBox(),
                widget.Prompt(),
                widget.WindowName(),
                widget.Chord(
                    chords_colors={
                        'launch': ("#ff0000", "#ffffff"),
                    },
                    name_transform=lambda name: name.upper(),
                ),
                widget.TextBox("default config", name="default"),
                widget.TextBox("Press &lt;M-r&gt; to spawn",
                               foreground="#d75f5f"),
                widget.Systray(),
                widget.Clock(format='%d-%m-%Y %a %I:%M %p'),
                widget.QuickExit(),
            ],
            24,
        ),
    ),
]
"""
# Drag floating layouts.
mouse = [
    Drag(
        [mod],
        "Button1",
        lazy.window.set_position_floating(),
        start=lazy.window.get_position()
    ),
    Drag(
        [mod],
        "Button3",
        lazy.window.set_size_floating(),
        start=lazy.window.get_size()
    ),
    Click([mod], "Button2", lazy.window.bring_to_front())
]


@hook.subscribe.startup_once
def autostart():
    subprocess.call(
        [path.join(path.join(path.expanduser('~'), ".config", "qtile"), 'autostart.sh')])


dgroups_key_binder = None
dgroups_app_rules = []  # type: List
main = None  # WARNING: this is deprecated and will be removed soon
follow_mouse_focus = False
bring_front_click = True
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    *layout.Floating.default_float_rules,
    Match(wm_class='confirmreset'),  # gitk
    Match(wm_class='makebranch'),  # gitk
    Match(wm_class='maketag'),  # gitk
    Match(wm_class='ssh-askpass'),  # ssh-askpass
    Match(title='branchdialog'),  # gitk
    Match(title='pinentry'),  # GPG key password entry
    Match(wm_class='confirm'),
    Match(wm_class='dialog'),
    Match(wm_class='download'),
    Match(wm_class='error'),
    Match(wm_class='file_progress'),
    Match(wm_class='notification'),
    Match(wm_class='splash'),
    Match(wm_class='toolbar'),
    Match(wm_class='Arandr'),
    Match(wm_class='feh')
], border_focus='6e0cad', border_normal='000000',fullscreen_border_width = 1, border_width = 1)
auto_fullscreen = True
focus_on_window_activation = "smart"
auto_minimize = True
reconfigure_screens = True

wmname = "LG3D"


# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
