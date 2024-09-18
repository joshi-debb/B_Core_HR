[Setup]
AppName=MiAplicacion
AppVersion=1.0
DefaultDirName={pf}\MiAplicacion
DefaultGroupName=MiAplicacion
OutputDir=userdocs:Inno Setup Examples Output
OutputBaseFilename=MiAplicacion_Setup
Compression=lzma
SolidCompression=yes

[Files]
Source: "C:\Users\why96\Desktop\B_Core_HR\dist\main.exe"; DestDir: "{app}"; Flags: ignoreversion

[Icons]
Name: "{group}\MiAplicacion"; Filename: "{app}\main.exe"
Name: "{userdesktop}\MiAplicacion"; Filename: "{app}\main.exe"

[Run]
Filename: "{app}\main.exe"; Description: "{cm:LaunchProgram,MiAplicacion}"; Flags: nowait postinstall skipifsilent
