# THIS SCRIPT MUST BE RUN FROM POWERSHELL AS AN ADMINSTRATOR
# (apologies that this is a powershell script - feel free to change to python using subprocess...)

# Read input args
param(
    [Parameter(Mandatory =$true)]
    [string]$ArgsFile
)

# Add standard prefix to args file path
$ArgsFile = ".\multi_file_run_lists\" + $ArgsFile

# Check args file exists
if (-not (Test-Path $ArgsFile)) {
    Write-Error "Argument file not found: $ArgsFile"
    exit 1
}

# Read args file, pipe into filter for empty lines
$argLines = Get-Content $ArgsFile | Where-Object {$_.Trim() -ne""} 

#For run metadata
$startTime = Get-Date
$counter = 1

$riValues = @{}

foreach ($line in $argLines) {

    $values = $line -split '\s+'
    $argArray = @(
        "--mm", $values[0],
        "--ms", $values[1],
        "--p", $values[2],
        "--ri", $values[3]
    )

    Write-Host "Checking arg combo is valid $argArray"
    Write-Host "`n"

    python test_args.py $argArray
    Write-Host "`n"

    $riValue = $values[3]
    
    # Check if --ri value has been used before
    if ($riValues.ContainsKey($riValue)) {
        Write-Host "ERROR: Duplicate --ri value detected: $riValue" -ForegroundColor Red
        Write-Host "This value was already used in a previous iteration." -ForegroundColor Red
        Write-Host "`n"
        exit 1
    }

    # Add to tracking hash
    $riValues[$riValue] = $true
}

Write-Host "All run ids are unique, nice one!"

Write-Host "Running master_wipl_runner.py for $($argLines.Count) files"
Write-Host "`n"

foreach ($line in $argLines) {
    Write-Host "-------------------------------NEW WIPL FILE-------------------------------"
    Write-Host "`n"
    Write-Host "-> Running $line"
    Write-Host "`n"
    $values = $line -split '\s+'
    $argArray = @(
        "--mm", $values[0],
        "--ms", $values[1],
        "--p", $values[2],
        "--ri", $values[3]
    )
    python single_pol_master_wipl_runner.py $argArray
    if ($LASTEXITCODE -ne 0) {
        write-Warning "Run failed for args: $line"
    }

    $elapsedTime = (Get-Date) - $startTime
    $elapsedSeconds = [math]::Round($elapsedTime.TotalSeconds,1)

    Write-Host "----------- WIPL FILE $counter COMPLETE, TIME ELAPSED $elapsedSeconds s --------------"
    Write-Host "`n"
    Write-Host "`n"

    $counter = $counter + 1
}

