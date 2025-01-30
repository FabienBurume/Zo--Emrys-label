# -*- coding: utf-8 -*-
#
# Projet: Zoé-Emrys Label
# Licence: MIT License
# Copyright (c) 2025 [Votre Nom]
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# [ajouter les conditions ici]
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import json


data = {
    "organisation": {
        "name": "Zoé-Emrys Label",
        "established": 2020,
        "description": "Votre partenaire pour des solutions informatiques efficaces."
    },
    "services": [
        {
            "name": "Dépannage informatique",
            "description": "Résolution rapide des problèmes matériels et logiciels."
        },
        {
            "name": "Assistance technique",
            "description": "Support à distance et sur site."
        }
    ],
    "values": [
        "Qualité",
        "Innovation",
        "Engagement"
    ]
}


def save_data(filename, data):
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)


save_data('data.json', data)