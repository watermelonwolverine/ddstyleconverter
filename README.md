About
=====

This is a prototype of a programs that allows you to change the style of DungeonDraft maps with the help of conversion files.

Conversion files are a sort of look-up map which tell the program how to conversion should be done.
For more information about creating conversion maps see "How to create conversion maps"

You can convert: materials to other materials, objects to other materials and so on. 
Currently supported are materials, objects, paths, patterns, portals, roofs, terrains and walls.

The underlying principle is that of a simple search and replace and can be used for all kinds of things. For example:
- Convert between asset styles like 2-Minute-Tabletop, Crosshead and Forgotten Adventures
- Convert between summer, winter, spring and fall

Installation: Windows
=====================

Step 1: Get the exe
-------------------

### Option 1: Download

Download one of the pre-built `ddstyleconverter.exe` files from `Releases`

Go to Step 2: Install program

### Option 2: Build it yourself

Install python3 (version >= 3.8) and add it to your PATH system environment variable.

You can check the version via CMD or powershell with:

`python --version`

Download or clone the repo.

Open a CMD instance inside the project root folder and create a virtual environment.

`python -m venv .\venv`

Activate the venv:

`.\venv\Scripts\activate`

Install pyInstaller package:

`pip install pyInstaller`

Run build file:

`.\scripts\build_for_windows.cmd`

You should now have a ddstyleconverter.exe file under dist. After the build succeeded you can delete the venv you
previously created.

Go to Step 2: Install program

Step 2: Install program
-----------------------

Create an empty folder where you want to install the program for example C:\ddstyleconverter

Copy ddstyleconverter.exe into that folder.

Optional:
Add the installation path to your PATH system environment variable.
This enables you to execute the program from anywhere which makes it much easier to use.

Uninstallation: Windows
=======================

Delete ddstyleconverter.exe file from the installation directory.

Remove the path to the installation directory from the PATH system environment variable.

Installation: Ubuntu 16.04 - 20.04
=================================

Optional: Install Python
------------------------

An up-to-date Ubuntu 20.04 should have python >= 3.8. Check it with:

`python3 --version`

From here on `pythonX` will be used as placeholder for the python you should use. Depending on your system you need to
replace `X` with `3`, `3.8`, `3.9` or `3.10` .

Install python version>=3.8 if not yet installed.

`sudo apt install pythonX`

Step 1: Get the executable
--------------------------

### Option 1: Download

Download one of the pre-built `ddstyleconverter` files from `Releases`

Go to Step 2: Install the files

### Option 2: Build it yourself

Install python if haven't already.

Download or clone repo.

Create a venv inside the repo:

`sudo apt install pythonX-venv`

`pythonX -m venv ./venv`

Activate venv:

`source venv/bin/activate`

Install pyInstaller:

`pythonX -m pip install pyInstaller`

Now run the build script:

`./scrips/build_for_ubuntu.sh`

Step 2: Install the files
-------------------------

Copy the `ddstyleconverter` file either from `dist` from where you downloaded it to `usr/bin/`

Make the file executable:

`sudo chmod ugo=rx usr/bin/ddstyleconverter`

Uninstallation: Ubuntu
======================

Delete the file /usr/bin/ddstyleconverter

Usage
=====

IMPORTANT:  
Add all the asset packs you need to the map before you do the conversion. 
If you try to open a map that has references to assets to an un-imported asset pack it will just load forever. 

Syntax
------

`ddstyleconverter [--verbose-info, --verbose-debug, --version, --help] target_path --out output_path --map map_path`

`target_path`: Path to the file which should be processed

`output_path`: File path to where the result should be written

`map_path`: Path to the conversion map file

Options
-------

`--verbose-info`: Enables verbose output to console

`--verbose-debug`: Enables very verbose output to console

`--version`: Print version and exits

`--help`: Display help and exit 

Examples
--------

Converting a map:

Ubuntu:
`ddstyleconverter path/to/file.dungeondraft_map --out path/to/output_file.dungeondraft_map --map path/to/conversion_map.json`

Windows:
`ddstyleconverter.exe path\to\file.dungeondraft_map --out path\to\output_file.dungeondraft_map --map path\to\conversion_map.json`

Known Issues and Quirks
=======================

Windows
-------

When one of the paths has `\'` at the end, the arguments will get mixed up. This is a problem with how python handles
arguments and probably can't be fixed. For example on Windows `ddstyleconverter.exe '\folder name with spaces\'`
will fail but `ddstyleconverter.exe '\folder name with spaces'` will succeed.

How To create conversion maps
=============================

Conversion maps are simple json files. Don't give up if you're not familiar with the json format. 
The json syntax is really easy to understand and requires zero programming knowledge. 
I recommend downloading and installing a text editor that supports the json format, for example Notepad++. 

Understanding the dungeondraft_map format
-----------------------------------------

Before we can create a conversion map we need to understand the format of dungeondraft_map files. 
Don't worry, it's really simple. 
Open up a dungeondraft_map file with your chosen text editor. 
If you are using Notepad++ tell the program that it should interpret the text as json via `Language > J > JSON`. 
What you will see is text in json format. Take a while to understand the basic format. 
The important parts are under `world/levels` (reading: Under `world` and there under `levels`), 
here you see the contents of each level. 
The contents are conveniently split into: `patterns, walls, portals, terrain, materials, paths, objects` and `roofs` 
Have a look at each of those entries. Most of them are lists (surrounded by `[]`) of simple sub-entries. 
For example an `objects` entry has the format: 

    {
        "position": "Vector2(1036, 1537.44)",
        "rotation": -0,
        "scale": "Vector2( 0.892452, 0.892356 )",
        "mirror": false,
        "texture": "res://packs/xjCzavyl/textures/objects/anvil_01.png",
        "layer": 100,
        "shadow": false,
        "block_light": false,
        "node_id": "26"
    }

The important parts here is the `texture` entry. That is what we want to replace. 

Creating new conversion maps
----------------------------

To create a conversion file create a new file and give it the file extension json. 
The basic format of a conversion map is:

    {
        "style_maps": {
            "materials": [],
            "objects": [],
            "paths": [],
            "patterns": [],
            "portals": [],
            "roofs": [],
            "terrain": [],
            "walls": []
        }
    }

Entries
-------
All entry types extend the same base entry, which has the format:

    {
        "from_texture": "",
        "to_texture": ""
    }

The `from_texture` and `to_texture` entries have to contain values from the respective 
`texture` entries from the dungeondraft_map file. 
For example an entry under `materials` would look like this:

    {
        "from_texture": "res://textures/materials/lava_tile.png",
        "to_texture": "res://packs/xjCzavyl/textures/materials/lava_tile.png"
    }

Which reads as: Replace all `texture` values within `materials` entries that have the value 
`res://textures/materials/lava_tile.png` with `res://packs/xjCzavyl/textures/materials/lava_tile.png`

The easiest way to find those `texture` values is to have a dungeondraft_map file which contains exactly two things:

1. The object/path/wall/etc you want to be replaced
2. The respective object/path/wall/etc with what you want to replace the first thing. You can only replace a path with path and an object with an object and so on.

I recommend putting them on different levels to make it easier to compare them. 
Such a dungeondraft_map file would look something like this: 

    {
        "header": {
            "creation_build": "1.0.3.2 tricky vampire",
            "creation_date": {
                "year": 2022,
                "month": 4,
                "day": 21,
                "weekday": 4,
                "dst": false,
                "hour": 11,
                "minute": 24,
                "second": 25
            },
            "uses_default_assets": true,
            "asset_manifest": [
                {
                    "name": "Crosshead",
                    "id": "xjCzavyl",
                    "version": "1",
                    "author": "Crosshead",
                    "custom_color_overrides": {
                        "enabled": false,
                        "min_redness": 0.1,
                        "min_saturation": 0,
                        "red_tolerance": 0.04
                    }
                }
            ],
            ...
        },
        "world": {
            ...
            "levels": {
                "0": {
                    "label": "Crosshead",
                    ...
                    "objects": [
                        {
                            "position": "Vector2( 1280, 2048 )",
                            "rotation": -0.698132,
                            "scale": "Vector2( 0.552237, 0.552487 )",
                            "mirror": false,
                            "texture": "res://packs/xjCzavyl/textures/objects/book_01.png",
                            "layer": 100,
                            "shadow": false,
                            "block_light": false,
                            "node_id": "2a"
                        }
                    ]
                    ...
                },
                "1": {
                    "label": "Ground",
                    ...
                    "objects": [
                        {
                            "position": "Vector2( 1280, 2048 )",
                            "rotation": 0,
                            "scale": "Vector2( 1, 1 )",
                            "mirror": false,
                            "texture": "res://textures/objects/activities/administration/book_04.png",
                            "layer": 100,
                            "shadow": false,
                            "block_light": false,
                            "node_id": "3d"
                        }
                    ],
                    ...
                }
            }
        }
    }

As you may notice both objects have completely different scales and rotations.
Because of that the `objects` entries of the conversion maps supports `rotation, translation` and `scale`

The `objects` entry to replace "res://textures/objects/activities/administration/book_04.png" with "res://packs/xjCzavyl/textures/objects/book_01.png" would look like this:

    {
        "from_texture": "res://textures/objects/activities/administration/book_04.png",
        "to_texture": "res://packs/xjCzavyl/textures/objects/book_01.png",
        "translation": "Vector2(-11.58, -1.95)",
        "rotation": -0.698132,
        "scale": "Vector2( 0.552237, 0.552237 )"
    }
