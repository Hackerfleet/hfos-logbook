#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# HFOS - Hackerfleet Operating System
# ===================================
# Copyright (C) 2011-2019 Heiko 'riot' Weinen <riot@c-base.org> and others.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

__author__ = "Heiko 'riot' Weinen"
__license__ = "AGPLv3"

from isomer.schemata.defaultform import editbuttons, section, horizontal_divider
from isomer.schemata.base import base_object

"""

Schema: LogbookEntry
===============

Contains
--------

Multiple logbook-entry and a general logbook schema.

See also
--------

Provisions


"""

LogbookEntrySchema = base_object('logbookentry')

LogbookEntrySchema['properties'].update({
    'coordinate': {
        'type': 'object',
        'properties': {
            "lat": {
                "type": "number",
                "maximum": 90,
                "minimum": -90,
                "title": "Latitude",
                "description": "Latitude of coordinate",
            },
            "lng": {
                "type": "number",
                "maximum": 180,
                "minimum": -180,
                "title": "Longitude",
                "description": "Longitude of coordinate",
            }
        }
    },
    'severity': {
        'type': 'string',
        'enum': ['Info', 'Warning', 'Critical'],
        'title': 'Severity',
        'default': 'Info'
    },
    'start': {
        'type': 'string', 'format': 'datetimepicker',
        'title': 'Event begin',
        'description': 'Date and time of event\'s begin'
    },
    'end': {
        'type': 'string', 'format': 'datetimepicker',
        'title': 'Event end',
        'description': 'Date and time of event\'s end'
    },
    'category': {
        'type': 'string', 'title': 'Category',
        'enum': ['Incident', 'Navigation', 'Technical', 'Bridge', 'Weather', 'Radio'],
        'description': 'Category of log event',
    },
    'notes': {
        'type': 'string', 'format': 'html', 'title': 'User notes',
        'description': 'Entry notes'
    },
    'weather': {
        'type': 'object',
        'properties': {
            'coverage': {
                'type': 'integer',
                'maximum': 8,
                'minimum': 0,
                'title': 'Cloud coverage',
                'description': '0-8/8 of cloud coverage'
            },
            'wind': {
                'type': 'object',
                'properties': {
                    'direction': {
                        'type': 'integer',
                        'maximum': 359,
                        'minimum': 0,
                        'title': 'Wind direction (°)'
                    },
                    'speed': {  # TODO: See https://github.com/Hackerfleet/hfos/issues/1
                        'type': 'integer',
                        'maximum': 250,
                        'minimum': 0,
                        'title': 'Wind speed (m/s)'
                    },
                    'gust': {
                        'type': 'integer',
                        'maximum': 250,
                        'minimum': 0,
                        'title': 'Gust speed (m/s)'
                    }
                }
            },
            'waves': {
                'type': 'array',
                'title': 'Waves',
                'items': {
                    'type': 'object',
                    'properties': {
                        'direction': {
                            'type': 'integer',
                            'maximum': 359,
                            'minimum': 0,
                            'title': 'Wave direction (°)'
                        },
                        'speed': {
                            # TODO: See https://github.com/Hackerfleet/hfos/issues/1
                            'type': 'integer',
                            'maximum': 250,
                            'minimum': 0,
                            'title': 'Wave speed (m/s)'
                        },
                        'height': {
                            'type': 'integer',
                            'maximum': 250,
                            'minimum': 0,
                            'title': 'Wave height (m)'
                        },
                        'distance': {
                            'type': 'integer',
                            'maximum': 5000,
                            'minimum': 0,
                            'title': 'Wave distance (m)'
                        }
                    }
                }
            },
            'barometer': {
                'type': 'integer',
                'minimum': 800,
                'maximum': 1200,
                'title': 'Barometer (hPa)',
                'description': 'Air pressure'
            },
            'thermometer': {
                'type': 'object',
                'properties': {
                    'air': {
                        'type': 'number',
                        'minimum': -90,
                        'maximum': 60,
                        'title': 'Air (°C)',
                        'description': 'Air temperature'
                    },
                    'water': {
                        'type': 'number',
                        'minimum': -2,
                        'maximum': 45,
                        'title': 'Water (°C)',
                        'description': 'Water temperature'
                    }
                }
            },
            'hygrometer': {
                'type': 'integer',
                'minimum': 0,
                'maximum': 100,
                'title': 'Humidity (%)',
                'description': 'Relative air humidity'
            }
        }
    },
    'bridge': {
        'type': 'object',
        'properties': {
            'subcategory': {
                'type': 'string',
                'enum': [
                    'Arrival',
                    'Departure',
                    'ManifestCrew',
                    'ObservationEnvironment',
                    'CrewSafetyBriefing',
                    'FirewatchEvent',
                    'InspectionEvent',
                    'LogcheckEvent',
                    'WatchEvent'
                ],
            },
        }
    },
    'technical': {
        'type': 'object',
        'properties': {
            'subcategory': {
                'type': 'string',
                'enum': [
                    'MachineRPM',
                    'MachineStatus',
                    'BatteryStatus',
                    'NavigationStatus',
                    'EmergencyEquipmentStatus',
                    'Breakdown',
                    'BunkerChange',
                    'BunkerLevel',
                    'EngineReading',
                    'OverhaulEvent'
                ]
            }
        }
    },
    'navigation': {
        'type': 'object',
        'properties': {
            'subcategory': {
                'type': 'string',
                'enum': [
                    'Course',
                    'CourseOverGround',
                    'SpeedOverWater',
                    'SpeedOverGround',
                    'SpeedCurrent',
                    'DriftCurrent',
                    'TidalData',
                    'Maneuver',
                    'FogSignal',
                    'FogBehaviour',
                    'LightsAndSignals',
                    'Anchoring',
                    'Towing',
                    'CourseChange',
                    'NavigationMark',
                    'Position',
                    'ShipMovements',
                    'ShipPosition',
                    'ShipSpeed',
                ]
            }

        }
    },
    'incident': {
        'type': 'object',
        'properties': {
            'subcategory': {
                'type': 'string',
                'enum': [
                    'Accident',
                    'CollisionIncident',
                    'DistressIncident',
                    'EngineIncident',
                    'PollutionIncident',
                    'SalvageIncident',
                    'SpillpreventionIncident',
                ]
            }
        }
    },
})

LogbookEntryForm = [
    section(2, 4, [
        [
            'start', 'end', 'category', 'severity'
        ],
        [
            'coordinate.lat', 'coordinate.lng',
        ]
    ]),
    horizontal_divider(),
    section(4, 3, [
        [
            'weather.wind.direction', 'weather.wind.speed', 'weather.wind.gust'
        ],
        [
            'weather.hygrometer', 'weather.thermometer.air',
            'weather.thermometer.water',
        ],
        [
            'weather.coverage', 'weather.barometer'
        ],
        [
            'weather.waves'
        ]
    ], condition="$ctrl.model.category === 'Weather'"),
    section(2, 3, [
        [
            'technical', 'technical.subcategory'
        ]
    ], condition="$ctrl.model.category === 'Technical'"),
    section(2, 3, [
        [
            'navigation', 'navigation.subcategory'
        ]
    ], condition="$ctrl.model.category === 'navigation'"),
    section(2, 3, [
        [
            'incident', 'incident.subcategory'
        ]
    ], condition="$ctrl.model.category === 'Incident'"),
    section(2, 3, [
        [
            'bridge', 'bridge.subcategory'
        ]
    ], condition="$ctrl.model.category === 'Bridge'"),

    'notes',
    editbuttons
]

LogbookEntry = {'schema': LogbookEntrySchema, 'form': LogbookEntryForm}
