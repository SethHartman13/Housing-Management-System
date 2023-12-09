## land_dict - CVAR

```jsonc
{
    "Test location": {
        "Location Details": {
            "PlotType": "Cannot Be Changed",
            "Tier": 1,
            "TotalBuildCost": -1,

            "Description": "Can be changed",
            "UpkeepCost": 1,
            "URL": "Can be changed",
            "Color": "Can be changed",
            "Size": "Can be changed",

            "Build": {
                "Tier": 2,
                "Time": 0,
                "Cost": 0,
                "Start": 0
            }

        "Test room": {
            "RoomType": "Cannot Be Changed",
            "Tier": 1,
            "TotalBuildCost": -1,

            "Description": "Can be changed",
            "UpkeepCost": 1,
            "URL": "Can be changed",
            "Color": "Can be changed",
            "Size": "Can be changed",

            "Build": {
                "Tier": 2,
                "Time": 0,
                "Cost": 0,
                "Start": 0
            }
        }
    }
}
```

-   `Test Location`: Plot of land entity (can be housing, a shop, guild, etc.)
    -   `Test room`: Name of the room on the plot of land
        -   `RoomType`: Room type, cannot be changed by player (Always Present)
        -   `Tier`: Tier number, cannot be changed by player (Always Present)
        -   `TotalBuildCost`: Total cost so far on room, cannot be changed by player (Always Present)
        -   `URL`: Image URL of room, can be changed by player, only present if changed
        -   `Color`: Color of room, can be changed by player, only present if changed
        -   `Size`: Size of room, can be changed by player, only present if changed
        -   `Build`: Generated only when during construction
            -   `Tier`: Tier being upgraded/built to, cannot be changed by player, always present
            -   `Time`: Time it takes to upgrade/build, can be changed by player, only present if changed
            -   `Cost`: Cost to upgrade/build, can be changed by player, only present if changed
            -   `Start`: Time construction started, always present

## lms_settings - SVAR

```json
{
    "Plots": ["SVAR example", "GVAR example"],
    "Rooms": ["SVAR example", "GVAR example"]
}
```

## SVAR/GVAR Plots

```jsonc
{
    "Test Plot": {
        "1": {
            "TierName": "String",
            "Description": "String",
            "BuildCost": 0,
            "UpkeepCost": 0,
            "Requirements": "String",
            "URL": "String",
            "Color": "String",
            "Benefits": "String",
            "Size": "String"
        }
    }
}
```

-   `TierName`: Every tier has this
-   `Description`: Applies to sequential tiers
-   `BuildCost`: Can pull from default settings
-   `Upkeep Cost`: Can pull from default settings
-   `Requirements`: Applies to sequential tiers
-   `URL`: Applies to sequential tiers
-   `Color`: Can pull from default settings
-   `Benefits`: Applies to sequential tiers
-   `Size`: Can pull from default settings

## lms_land_settings - SVAR

```json
{
    "BuildTime": {
        "TimePeriodPerCost": 86400,
        "Cost": 2000,
        "Round": 1
    },
    "Size": {
        "Basic": "1x1",
        "Fine": "1x2",
        "Fancy": "2x2",
        "Exquisite": "2x3",
        "Luxury": "3x3"
    },
    "Cost": {
        "Basic": 5000,
        "Fine": 10000,
        "Fancy": 20000,
        "Exquisite": 40000,
        "Luxury": 80000
    },
    "Color": {
        "Basic": "#242528",
        "Fine": "#1FC219",
        "Fancy": "#4990E2",
        "Exquisite": "#9810E0",
        "Luxury": "#FEA227"
    },
    "Upkeep": {
        "TimePeriod": 604800,
        "Basic": 0,
        "Fine": 0,
        "Fancy": 0,
        "Exquisite": 0,
        "Luxury": 0
    }
}
```

-   `Rooms`: List of GVAR/SVARs
-   `Settings`: General settings
    -   `BuildTime`: Buildtime is determined by seconds/gold (i.e. 1 day of build time per 2000 gold)
        -   `Cost`: Cost in Gold
        -   `Time`: Time in seconds
        -   `Round`: Tribol on whether to round up or down:
            -   `1`: Round up
            -   `0`: Don't round
            -   `-1`: Round down
    -   `UpkeepRate`: Sets how often upkeep is collected (i.e. if upkeep of a room is 50gp, the upkeep rate could be 1 week... and it sets upkeep to 50gp per 1 week)
    -   `Defaults`: Room defaults
        -   `Size`: Default room size by tier
        -   `Cost`: Default room cost by tier
        -   `Color`: Default room color by tier
        -   `Upkeep`: Default upkeep cost by tier

## SVAR/GVAR Rooms

```jsonc
{
    "Test Room": {
        "1": {
            "TierName": "String",
            "Description": "String",
            "BuildCost": 0,
            "UpkeepCost": 0,
            "Requirements": "String",
            "URL": "String",
            "Color": "String",
            "Benefits": "String",
            "Size": "String"
        }
    }
}
```

-   `TierName`: Every tier has this
-   `Description`: Applies to sequential tiers
-   `BuildCost`: Can pull from default settings
-   `Upkeep Cost`: Can pull from default settings
-   `Requirements`: Applies to sequential tiers
-   `URL`: Applies to sequential tiers
-   `Color`: Can pull from default settings
-   `Benefits`: Applies to sequential tiers
-   `Size`: Can pull from default settings

## lms_room_settings - SVAR

```json
{
    "BuildTime": {
        "TimePeriodPerCost": 0,
        "Cost": 2000,
        "Round": 1
    },
    "Size": {
        "Basic": "10x10",
        "Fine": "10x15",
        "Fancy": "15x15",
        "Exquisite": "15x20",
        "Luxury": "20x20"
    },
    "Cost": {
        "Basic": 5000,
        "Fine": 10000,
        "Fancy": 20000,
        "Exquisite": 40000,
        "Luxury": 80000
    },
    "Color": {
        "Basic": "#242528",
        "Fine": "#1FC219",
        "Fancy": "#4990E2",
        "Exquisite": "#9810E0",
        "Luxury": "#FEA227"
    },
    "Upkeep": {
        "TimePeriod": 604800,
        "Basic": 0,
        "Fine": 0,
        "Fancy": 0,
        "Exquisite": 0,
        "Luxury": 0
    }
}
```
