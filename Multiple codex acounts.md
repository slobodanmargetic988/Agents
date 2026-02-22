You might want to switch between accounts on your Codex for whatever reason.
You can avoid logging in and out by having separate .codex folders.
I use .codex, .codex-profile2, and .codex-originalprofile, for example. The really important file in these folders is auth.json, which is used to authenticate. Using Codex CLI with another account is as simple as passing a home variable to it, and there are examples of this in the thread-dispatch skill. But the Codex desktop app will always use the auth.json from .codex, so I made this quick profile-switch script. All the .codex-profile folders and .codex-original should be in the same folder.

When creating .codex-profile2, you can copy the whole .codex folder with a new name, but instead you might want to replace some files in the new folder with symlinks to the original folder, for example the AGENTS.md file and the entire skills folder. That way you won't have to install the same skills in both profiles or forget to install them. You might also want config.toml to be a link, or you might want it specifically set up differently for different profiles.

## create the script

New-Item -ItemType Directory -Force -Path "$env:USERPROFILE/bin" | Out-Null
@'
param(
  [Parameter(Mandatory = $true)]
  [string]$Profile
)

$Base = "$env:USERPROFILE/.codex"
$SrcDir = "$env:USERPROFILE/.codex-$Profile"
$SrcAuth = "$SrcDir/auth.json"
$DstAuth = "$Base/auth.json"

if (-not (Test-Path $Base -PathType Container)) {
  Write-Error "Error: $Base does not exist"
  exit 1
}

if (-not (Test-Path $SrcAuth -PathType Leaf)) {
  Write-Error "Error: $SrcAuth not found"
  exit 1
}

if (Test-Path $DstAuth -PathType Leaf) {
  $timestamp = Get-Date -Format "yyyyMMddHHmmss"
  Copy-Item -Force $DstAuth "$Base/auth.json.bak.$timestamp"
}

Copy-Item -Force $SrcAuth $DstAuth

Write-Host "Switched Codex auth to profile: $Profile"
Write-Host "Source: $SrcAuth"
Write-Host "Target: $DstAuth"
'@ | Set-Content -Encoding UTF8 "$env:USERPROFILE/bin/switch-codex-profile.ps1"


## make executable and use 

Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
Set-Alias switchCodex "$env:USERPROFILE/bin/switch-codex-profile.ps1"
switchCodex profile2
