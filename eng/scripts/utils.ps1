Set-StrictMode -version 2.0
$ErrorActionPreference = "Stop"

$repo_dir = Resolve-Path (Join-Path $PSScriptRoot "../..")
# $src_dir = Resolve-Path (Join-Path $repo_dir "src")
# $test_dir = Resolve-Path (Join-Path $repo_dir "test")
$on_agent = $false;

if ($env:GITHUB_ACTIONS) {
    $on_agent = $true;
}

$temp_dir = Join-Path $repo_dir "_temp";

$agent_temp_dir = $env:AGENT_TEMPDIRECTORY;

if ($agent_temp_dir) {
    $temp_dir = $agenttemp_directory;
}

function Exec([scriptblock]$cmd, [string]$errorMessage = "Error executing command: " + $cmd) { 
    & $cmd

    if ((-not $?) -or ($lastexitcode -ne 0)) {
        throw $errorMessage 
    }
}