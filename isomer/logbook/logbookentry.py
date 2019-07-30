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

from isomer.schemata.defaultform import defaultform
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
                "title": "Latitude of coordinate.",
                "description": "",
            },
            "lng": {
                "type": "number",
                "maximum": -180,
                "minimum": 180,
                "title": "Longitude of coordinate.",
                "description": "",
            }
        }
    },
    'severity': {
        'type': 'string',
        'enum': ['Info', 'Warning', 'Critical'],
        'default': 'Info',
        'x-schema-form': {
            'type': 'select',
            'titleMap': {
                'Info': 'Info',
                'Warning': 'Warning',
                'Critical': 'Critical'
            }
        }
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
        'enum': ['Incident', 'Navigation', 'Technical', 'Bridge', 'Weather'],
        'description': 'Category of log event',
        'x-schema-form': {
            'type': 'select',
            'titleMap': {
                'Incident': 'Incident',
                'Navigation': 'Navigation',
                'Technical': 'Technical',
                'Bridge': 'Bridge',
                'Weather': 'Weather'
            }
        }
    },
    'subcategory': {
        'type': 'string', 'title': 'Sub Category',
        'description': 'Sub Category of log event'
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
                'max': 8,
                'min': 0,
                'title': 'Cloud coverage',
                'description': '0-8/8 of cloud coverage'
            },
            'wind': {
                'type': 'object',
                'properties': {
                    'direction': {
                        'type': 'integer',
                        'max': 359,
                        'min': 0,
                        'title': 'Wind speed (°)'
                    },
                    'speed': {  # TODO: See https://github.com/Hackerfleet/hfos/issues/1
                        'type': 'integer',
                        'max': 250,
                        'min': 0,
                        'title': 'Wind speed (m/s)'
                    },
                    'gust': {
                        'type': 'integer',
                        'max': 250,
                        'min': 0,
                        'title': 'Gust speed (m/s)'
                    }
                }
            },
            'waves': {
                'type': 'array',
                'items': {
                    'type': 'object',
                    'properties': {
                        'direction': {
                            'type': 'integer',
                            'max': 359,
                            'min': 0,
                            'title': 'Wave direction (°)'
                        },
                        'speed': {
                            # TODO: See https://github.com/Hackerfleet/hfos/issues/1
                            'type': 'integer',
                            'max': 250,
                            'min': 0,
                            'title': 'Wave speed (m/s)'
                        },
                        'height': {
                            'type': 'integer',
                            'max': 250,
                            'min': 0,
                            'title': 'Wave height (m)'
                        },
                        'distance': {
                            'type': 'integer',
                            'max': 5000,
                            'min': 0,
                            'title': 'Wave distance (m)'
                        }
                    }
                }
            },
            'barometer': {
                'type': 'integer',
                'min': 800,
                'max': 1200,
                'title': 'Barometer (hPa)',
                'description': 'Air pressure'
            },
            'thermometer': {
                'type': 'object',
                'properties': {
                    'air': {
                        'type': 'float',
                        'min': -90,
                        'max': 60,
                        'title': 'Air (°C)',
                        'description': 'Air temperature'
                    },
                    'water': {
                        'type': 'float',
                        'min': -2,
                        'max': 45,
                        'title': 'Water (°C)',
                        'description': 'Water temperature'
                    }
                }
            },
            'hygrometer': {
                'type': 'integer',
                'min': 0,
                'max': 100,
                'title': 'Humidity (%)',
                'description': 'Relative air humidity'
            }
        }
    },
    'bridge': {
        'type': 'object',
        'properties': {
            'text': {
                'type': 'text',
                'title': 'Entry',
                'description': 'Bridge entry custom text'
            }
        }
    },
    'technical': {
        'type': 'object',
        'properties': {

        }
    },
    'navigation': {
        'type': 'object',
        'properties': {
        }
    },
    'incident': {
        'type': 'object',
        'properties': {

        }
    },
})

LogbookEntry = {'schema': LogbookEntrySchema, 'form': defaultform}
