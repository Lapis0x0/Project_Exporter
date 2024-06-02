# dmg_settings.py

import os

application_name = "ProjectExportTool"
app_path = f"dist/dmg/{application_name}.app"
icon_path = "icon/macos.icns"  # 这里设置你的.icns图标文件路径

# Basic options
settings = {
    'app': app_path,
    'icon': icon_path,
    'format': 'UDZO',
    'compression-level': 9,
    'background': None,
    'show-status-bar': False,
    'show-tab-view': False,
    'show-pathbar': False,
    'sidebar-width': 180,
    'window': {
        'position': (100, 100),
        'size': (640, 480),
        'default-view': 'icon-view',
    },
    'code-signing': {
        'identity': None,
        'timestamp': None,
        'requirements': None,
    },
    'license': None,
    'create-dmg': {
        'applications-link': '/Applications',
        'icon-size': 128,
        'icon': {
            'app': {
                'position': (140, 120),
                'icon': icon_path,
            },
            'Applications': {
                'position': (500, 120),
                'icon': '/System/Library/CoreServices/CoreTypes.bundle/Contents/Resources/SidebarApplicationsFolder.icns',
            },
        },
    },
}
