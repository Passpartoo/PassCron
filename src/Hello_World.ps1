#
# Passpartoo - scripting programme
# 
############################################
# PowerShell Programme
############################################
# Version du script 1.0
############################################


<#
Documentation:
File test for AutomationScript.py
#>

$intro = @"

**************************************************
*		    Hello World 		                 *
**************************************************
"@

Clear-Host

write-host $intro -ForegroundColor Green

$Texte="Hello World test script Begin !" 
Write-host $Texte

Write-host "Nous sommes le" $(Get-Date) -NoNewline
echo ""
Write-Host "Repertoire de travail : " $(Get-Location)
echo ""
echo ""
Add-Type -AssemblyName System.Windows.Forms
[System.Windows.Forms.MessageBox]::Show('Bonjour tous le monde', 'Hello World')
