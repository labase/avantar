""" Configuration for project Avantar.

Changelog
---------
.. versionadded::    23.09
    |br| first version of config (01)

|   **Open Source Notification:** This file is part of open source program **AVANTAR**
|   **Copyright © 2023  Carlo Oliveira** <carlo@nce.ufrj.br>,
|   **SPDX-License-Identifier:** `GNU General Public License v3.0 or later <https://is.gd/3Udt>`_.
|   `Labase <http://labase.selfip.org/>`_ - `NCE <https://portal.nce.ufrj.br>`_ - `UFRJ <https://ufrj.br/>`_.

.. codeauthor:: Carlo Oliveira <carlo@nce.ufrj.br>

"""
from io import StringIO

import toml
import yaml

toml_str = """
title = "TOML Example"

[owner]
name = "Tom Preston-Werner"
dob = 1979-05-27T07:32:00-08:00

[database]
enabled = true
ports = [ 8000, 8001, 8002 ]
data = [ ["delta", "phi"], [3.14] ]
temp_targets = { cpu = 79.5, case = 72.0 }

[servers]

[servers.alpha]
ip = "10.0.0.1"
role = "frontend"

[servers.beta]
ip = "10.0.0.2"
role = "backend"
"""
output = StringIO()
data = toml.loads(toml_str)
emb = dict(d=[1, dict(d=[2, dict(f=[3, dict(g=[4, dict(Class=5, style=dict(top="3%"))])])])])
# emb = dict(d=[1, dict(c=[2, 3])])
# tdata = toml.dumps(emb)
# with open(output, "w") as out:
tdata = yaml.safe_dump(emb, output)
output.seek(0)
# output.close()
if __name__ == '__main__':
    print(data)
    print(tdata)
    print(output.read())

