# THIS SCRIPT MUST BE RUN FROM POWERSHELL AS AN ADMINSTRATOR
# (apologies that this is a powershell script - feel free to change to python using subprocess...)

# Read input args
param(
    [Parameter(Mandatory =$true)]
    [string]$ArgsFile
)

#Add standard prefix to args file path
$ArgsFile = ".\multi_file_run_lists\" + $ArgsFile

# Check args file exists
if (-not (Test-Path $ArgsFile)) {
    Write-Error "Argument file not found: $ArgsFile"
    exit 1
}

# Read args file, pipe into filter for empty lines)
$argLines = Get-Content $ArgsFile | Where-Object {$_.Trim() -ne""} 

Write-Host "Running master_wipl_runner.py for $($argLines.Count) files"

#For run metadata
$startTime = Get-Date
$counter = 1

foreach ($line in $argLines) {
    Write-Host "-------------------------------NEW WIPL FILE-------------------------------"
    Write-Host "-> Running $line"
    $values = $line -split '\s+'
    $argArray = @(
        "--mm", $values[0],
        "--ms", $values[1],
        "--p", $values[2],
        "--ri", $values[3]
    )
    python master_wipl_runner.py $argArray
    if ($LASTEXITCODE -ne 0) {
        write-Warning "Run failed for args: $line"
    }

    $elapsedTime = (Get-Date) - $startTime
    $elapsedSeconds = [math]::Round($elapsedTime.TotalSeconds,1)

    Write-Host "----------- WIPL FILE $counter COMPLETE, TIME ELAPSED $elapsedSeconds s --------------"
}

