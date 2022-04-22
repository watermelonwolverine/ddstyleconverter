from cli_wrapper.__args import verbose_info_option, verbose_debug_option, version_option, help_option, out_arg, conversion_map_arg
from cli_wrapper.__constants import app_name

about = "\
About\n\
=====\n\
\n\
This is a prototype of a program that allows you to change the style of DungeonDraft maps with the help of conversion files.\n\
\n\
A conversion file is a sort of look-up map which tell the program how to conversion should be done.\n\
For more information about creating conversion maps see \"How to create conversion maps\"\n\
\n\
You can convert: materials to other materials, objects to other materials and so on. \n\
Currently supported are materials, objects, paths, patterns, portals, roofs, terrains and walls.\n\
\n\
The underlying principle is that of a simple search and replace and can be used for all kinds of things. For example:\n\
- Convert between asset styles like 2-Minute-Tabletop, Crosshead and Forgotten Adventures\n\
- Convert between summer, winter, spring and fall"

usage = "\
Usage\n\
=====\n\
\n\
IMPORTANT:  \n\
Add all the asset packs you need to the map before you do the conversion. \n\
If you try to open a map that has references to assets of an un-imported asset pack it will just load forever. \n\
\n\
Syntax\n\
------\n\
\n\
`{0} [{1}, {2}, {3}, {4}] target_path {5} output_path {6} conversion_map_path`\n\
\n\
`target_path`: Path to the file which should be processed.\n\
\n\
`output_path`: File path to where the result should be written. The file itself must not exist but the parent directory must.\n\
\n\
`conversion_map_path`: Path to the conversion map file.\n\
\n\
Options\n\
-------\n\
\n\
`{1}`: Enables verbose output to console\n\
\n\
`{2}`: Enables very verbose output to console\n\
\n\
`{3}`: Print version and exits\n\
\n\
`{4}`: Display help and exit \n\
\n\
Examples\n\
--------\n\
\n\
Converting a map:\n\
\n\
Ubuntu:\n\
`{0} path/to/file.dungeondraft_map {5} path/to/output_file.dungeondraft_map {6} path/to/conversion_map.json`\n\
\n\
Windows:\n\
`{0}.exe path\\to\\file.dungeondraft_map {5} path\\to\\output_file.dungeondraft_map {6} path\\to\\conversion_map.json`".format(
    app_name,
    verbose_info_option,
    verbose_debug_option,
    version_option,
    help_option,
    out_arg,
    conversion_map_arg)

issues = "\
Known Issues and Quirks\n\
=======================\n\
\n\
Windows\n\
-------\n\
\n\
When one of the paths has `\\'` at the end, the arguments will get mixed up. This is a problem with how python handles\n\
arguments and probably can't be fixed. For example on Windows `{0}.exe '\\folder name with spaces\\'`\n\
will fail but `{0}.exe '\\folder name with spaces'` will succeed.".format(app_name)

installation_windows = "\
Installation: Windows\n\
=====================\n\
\n\
Step 1: Get the exe\n\
-------------------\n\
\n\
### Option 1: Download\n\
\n\
Download one of the pre-built `{0}.exe` files from `Releases`\n\
\n\
Go to Step 2: Install program\n\
\n\
### Option 2: Build it yourself\n\
\n\
Install python3 (version >= 3.8) and add it to your PATH system environment variable.\n\
\n\
You can check the version via CMD or powershell with:\n\
\n\
`python --version`\n\
\n\
Download or clone the repo.\n\
\n\
Open a CMD instance inside the project root folder and create a virtual environment.\n\
\n\
`python -m venv .\\venv`\n\
\n\
Activate the venv:\n\
\n\
`.\\venv\\Scripts\\activate`\n\
\n\
Install pyInstaller package:\n\
\n\
`pip install pyInstaller`\n\
\n\
Run build file:\n\
\n\
`.\\scripts\\build_for_windows.cmd`\n\
\n\
You should now have a {0}.exe file under dist. After the build succeeded you can delete the venv you\n\
previously created.\n\
\n\
Go to Step 2: Install program\n\
\n\
Step 2: Install program\n\
-----------------------\n\
\n\
Create an empty folder where you want to install the program for example C:\\{0}\n\
\n\
Copy {0}.exe into that folder.\n\
\n\
Optional:\n\
Add the installation path to your PATH system environment variable.\n\
This enables you to execute the program from anywhere which makes it much easier to use.\n\
\n\
Uninstallation: Windows\n\
=======================\n\
\n\
Delete {0}.exe file from the installation directory.\n\
\n\
Optional: Remove the path to the installation directory from the PATH system environment variable.".format(app_name)

installation_ubuntu = "Installation: Ubuntu 16.04 - 20.04\n\
=================================\n\
\n\
Optional: Install Python\n\
------------------------\n\
\n\
An up-to-date Ubuntu 20.04 should have python >= 3.8. Check it with:\n\
\n\
`python3 --version`\n\
\n\
From here on `pythonX` will be used as placeholder for the python you should use. Depending on your system you need to\n\
replace `X` with `3`, `3.8`, `3.9` or `3.10` .\n\
\n\
Install python version>=3.8 if not yet installed.\n\
\n\
`sudo apt install pythonX`\n\
\n\
Step 1: Get the executable\n\
--------------------------\n\
\n\
### Option 1: Download\n\
\n\
Download one of the pre-built `{0}` files from `Releases`\n\
\n\
Go to Step 2: Install the files\n\
\n\
### Option 2: Build it yourself\n\
\n\
Install python if haven't already.\n\
\n\
Download or clone repo.\n\
\n\
Create a venv inside the repo:\n\
\n\
`sudo apt install pythonX-venv`\n\
\n\
`pythonX -m venv ./venv`\n\
\n\
Activate venv:\n\
\n\
`source venv/bin/activate`\n\
\n\
Install pyInstaller:\n\
\n\
`pythonX -m pip install pyInstaller`\n\
\n\
Now run the build script:\n\
\n\
`./scrips/build_for_ubuntu.sh`\n\
\n\
Step 2: Install the files\n\
-------------------------\n\
\n\
Copy the `{0}` file either from `dist` from where you downloaded it to `usr/bin/`\n\
\n\
Make the file executable:\n\
\n\
`sudo chmod ugo=rx usr/bin/{0}`\n\
\n\
Uninstallation: Ubuntu\n\
======================\n\
\n\
Delete the file /usr/bin/{0}".format(app_name)

how_to_create_conversion_maps = "\
How To create conversion maps\n\
=============================\n\
\n\
Conversion maps are simple json files. Don't give up if you're not familiar with the json format. \n\
The json syntax is really easy to understand and requires zero programming knowledge. \n\
I recommend downloading and installing a text editor that supports the json format, for example Notepad++. \n\
\n\
Understanding the dungeondraft_map format\n\
-----------------------------------------\n\
\n\
Before we can create a conversion map we need to understand the format of dungeondraft_map files. \n\
Don't worry, it's really simple. \n\
Open up a dungeondraft_map file with your chosen text editor. \n\
If you are using Notepad++ tell the program that it should interpret the text as json via `Language > J > JSON`. \n\
What you will see is text in json format. Take a while to understand the basic format. \n\
The important parts are under `world/levels` (reading: Under `world` and there under `levels`), \n\
here you see the contents of each level. \n\
The contents are conveniently split into: `patterns, walls, portals, terrain, materials, paths, objects` and `roofs` \n\
Have a look at each of those entries. Most of them are lists (surrounded by `[]`) of simple sub-entries. \n\
For example an `objects` entry has the format: \n\
\n\
    {\n\
        \"position\": \"Vector2(1036, 1537.44)\",\n\
        \"rotation\": -0,\n\
        \"scale\": \"Vector2( 0.892452, 0.892356 )\",\n\
        \"mirror\": false,\n\
        \"texture\": \"res://packs/xjCzavyl/textures/objects/anvil_01.png\",\n\
        \"layer\": 100,\n\
        \"shadow\": false,\n\
        \"block_light\": false,\n\
        \"node_id\": \"26\"\n\
    }\n\
\n\
The important parts here is the `texture` entry. That is what we want to replace. \n\
\n\
Creating new conversion maps\n\
----------------------------\n\
\n\
To create a conversion file create a new file and give it the file extension json. \n\
The basic format of a conversion map is:\n\
\n\
    {\n\
        \"style_maps\": {\n\
            \"materials\": [],\n\
            \"objects\": [],\n\
            \"paths\": [],\n\
            \"patterns\": [],\n\
            \"portals\": [],\n\
            \"roofs\": [],\n\
            \"terrain\": [],\n\
            \"walls\": []\n\
        }\n\
    }\n\
\n\
Entries\n\
-------\n\
All entry types extend the same base entry, which has the format:\n\
\n\
    {\n\
        \"from_texture\": \"\",\n\
        \"to_texture\": \"\"\n\
    }\n\
\n\
The `from_texture` and `to_texture` entries have to contain values from the respective \n\
`texture` entries from the dungeondraft_map file. \n\
For example an entry under `materials` would look like this:\n\
\n\
    {\n\
        \"from_texture\": \"res://textures/materials/lava_tile.png\",\n\
        \"to_texture\": \"res://packs/xjCzavyl/textures/materials/lava_tile.png\"\n\
    }\n\
\n\
Which reads as: Replace all `texture` values within `materials` entries that have the value \n\
`res://textures/materials/lava_tile.png` with `res://packs/xjCzavyl/textures/materials/lava_tile.png`\n\
\n\
The easiest way to find those `texture` values is to have a dungeondraft_map file which contains exactly two things:\n\
\n\
1. The object/path/wall/etc you want to be replaced\n\
2. The respective object/path/wall/etc with what you want to replace the first thing. You can only replace a path with path and an object with an object and so on.\n\
\n\
I recommend putting them on different levels to make it easier to compare them. \n\
Such a dungeondraft_map file would look something like this: \n\
\n\
    {\n\
        \"header\": {\n\
            \"creation_build\": \"1.0.3.2 tricky vampire\",\n\
            \"creation_date\": {\n\
                \"year\": 2022,\n\
                \"month\": 4,\n\
                \"day\": 21,\n\
                \"weekday\": 4,\n\
                \"dst\": false,\n\
                \"hour\": 11,\n\
                \"minute\": 24,\n\
                \"second\": 25\n\
            },\n\
            \"uses_default_assets\": true,\n\
            \"asset_manifest\": [\n\
                {\n\
                    \"name\": \"Crosshead\",\n\
                    \"id\": \"xjCzavyl\",\n\
                    \"version\": \"1\",\n\
                    \"author\": \"Crosshead\",\n\
                    \"custom_color_overrides\": {\n\
                        \"enabled\": false,\n\
                        \"min_redness\": 0.1,\n\
                        \"min_saturation\": 0,\n\
                        \"red_tolerance\": 0.04\n\
                    }\n\
                }\n\
            ],\n\
            ...\n\
        },\n\
        \"world\": {\n\
            ...\n\
            \"levels\": {\n\
                \"0\": {\n\
                    \"label\": \"Crosshead\",\n\
                    ...\n\
                    \"objects\": [\n\
                        {\n\
                            \"position\": \"Vector2( 1280, 2048 )\",\n\
                            \"rotation\": -0.698132,\n\
                            \"scale\": \"Vector2( 0.552237, 0.552487 )\",\n\
                            \"mirror\": false,\n\
                            \"texture\": \"res://packs/xjCzavyl/textures/objects/book_01.png\",\n\
                            \"layer\": 100,\n\
                            \"shadow\": false,\n\
                            \"block_light\": false,\n\
                            \"node_id\": \"2a\"\n\
                        }\n\
                    ]\n\
                    ...\n\
                },\n\
                \"1\": {\n\
                    \"label\": \"Ground\",\n\
                    ...\n\
                    \"objects\": [\n\
                        {\n\
                            \"position\": \"Vector2( 1280, 2048 )\",\n\
                            \"rotation\": 0,\n\
                            \"scale\": \"Vector2( 1, 1 )\",\n\
                            \"mirror\": false,\n\
                            \"texture\": \"res://textures/objects/activities/administration/book_04.png\",\n\
                            \"layer\": 100,\n\
                            \"shadow\": false,\n\
                            \"block_light\": false,\n\
                            \"node_id\": \"3d\"\n\
                        }\n\
                    ],\n\
                    ...\n\
                }\n\
            }\n\
        }\n\
    }\n\
\n\
As you may notice both objects have completely different scales and rotations.\n\
Because of that the `objects` entries of the conversion maps supports `rotation, translation` and `scale`\n\
\n\
The `objects` entry to replace \"res://textures/objects/activities/administration/book_04.png\" with \"res://packs/xjCzavyl/textures/objects/book_01.png\" would look like this:\n\
\n\
    {\n\
        \"from_texture\": \"res://textures/objects/activities/administration/book_04.png\",\n\
        \"to_texture\": \"res://packs/xjCzavyl/textures/objects/book_01.png\",\n\
        \"translation\": \"Vector2(-11.58, -1.95)\",\n\
        \"rotation\": -0.698132,\n\
        \"scale\": \"Vector2( 0.552237, 0.552237 )\"\n\
    }\n\
"

installation = "\
{0}\n\
\n\
{1}".format(installation_windows, installation_ubuntu)

help_text = "\
%s\n\
\n\
%s\n\
\n\
%s\n\
\n\
%s" % (about, usage, issues, how_to_create_conversion_maps)

read_me = "\
%s\n\
\n\
%s\n\
\n\
%s\n\
\n\
%s\n\
\n\
%s" % (about, installation, usage, issues, how_to_create_conversion_maps)

read_me_for_ubuntu = "\
%s\n\
\n\
%s\n\
\n\
%s\n\
\n\
%s\n\
\n\
%s" % (about, installation_ubuntu, usage, issues, how_to_create_conversion_maps)

read_me_for_windows = "\
%s\n\
\n\
%s\n\
\n\
%s\n\
\n\
%s\n\
\n\
%s" % (about, installation_windows, usage, issues, how_to_create_conversion_maps)
