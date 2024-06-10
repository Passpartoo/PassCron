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
Gestion et export de l'historique avant de nettoyer le cache

#>

$intro = @"

**************************************************
*		Log & Cache History		                 *
**************************************************
"@

Clear-Host

write-host $intro -ForegroundColor Green

# Aller dans le répertoire de travail
#cd "C:\Users\user"


$History = (Get-PSReadLineOption).HistorySavePath
$History

Remove-Item -Path $History -Verbose

$old_History = Import-Csv -Path '.\CommandHistory.Csv'
 
Add-History -InputObject $OldHistory -Passthru

Clear-History

echo "Fin du programme"
