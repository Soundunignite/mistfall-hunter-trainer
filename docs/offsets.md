# Offsets — Mistfall Hunter 2026.01

Run `python -m src.tools.offset_dumper` after every game patch. The tool
scans the module for known signatures and writes resolved addresses to
`offsets.json`.

| Name         | Offset      | Notes                    |
|--------------|-------------|--------------------------|
| local_player | 0x02A1B3C0  | pointer to player struct |
| entity_list  | 0x02A1B420  | array of 512 entities    |
| view_matrix  | 0x02A2C010  | 4x4 float32              |
| health       | +0x1A8      | relative to player base  |
| position     | +0x2C0      | Vec3                     |
| rotation     | +0x2D8      | yaw/pitch                |
| team         | +0x318      | uint8                    |

If a signature fails to resolve, the trainer will refuse to attach and log
a warning. Do not ship hardcoded offsets without a matching build tag.