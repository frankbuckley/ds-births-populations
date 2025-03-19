Set-StrictMode -version 2.0
$ErrorActionPreference="Stop"

function Clean()
{
    . (Join-Path $PSScriptRoot "utils.ps1")
    Get-ChildItem $repo_dir -include bin,obj,AppPackages,BundleArtifacts,TestResults,.tools,_temp,node_modules,__publish -Recurse | ForEach-Object { Remove-Item $_.FullName -Force -Recurse }
}

try
{
    Clean
}
catch
{
    Write-Host $_
    Write-Host $_.Exception
    exit 1
}
