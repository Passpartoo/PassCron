#
# Passpartoo - scripting programme
# 
############################################
# PowerShell Programme 
############################################
# Version du script 1.0
############################################


<#
Documentation :
Script d'installation DHCP
https://www.it-connect.fr/cours/dhcp-du-protocole-a-la-configuration/

#>


$PROGNAMME = @"

**************************************************
*		      DHCP INSTALLER	         *
**************************************************

Ce script permet d'installer un DHCP en commande Shell

"@


$intro = @"
$PROGNAMME


"@


Clear-Host

write-host $intro -ForegroundColor Green

$Texte="Hello World, DHCP Installer Begin !" 
Write-host $Texte

# Aller dans le répertoire de travail
$WorkingDirectory = "C:\Users\temp"
cd $WorkingDirectory


Write-host "Nous sommes le" $(Get-Date) -NoNewline
echo ""
Write-Host "Répertoire de travail : " $(Get-Location)
echo ""
echo ""


#echo "Installer DHCP via PowerShell"

$dhcpName = "<nom-serveur-dhcp>"
$dhcpAdresse = "<adresse-ip-serveur-dhcp>"

Install-WindowsFeature -Name DHCP -IncludeManagementTools

# Via netsh
netsh dhcp add securitygroups
# (ou) via PowerShell
Add-DhcpServerSecurityGroup

#On redémarre le service DHCP dans le but d'assurer la prise en compte des changements :

Restart-Service dhcpserver

#Dans le cas d'un environnement Active Directory avec un domaine, autoriser le serveur DHCP dans l'annuaire.

Add-DhcpServerInDC -DnsName $dhcpName -IPAddress $dhcpAdresse

#Par exemple, comme mon serveur se nomme "SRV01.it-connect.fr" et a pour adresse IPv4 "192.168.1.210" cela donnera :

Add-DhcpServerInDC -DnsName SRV01.it-connect.fr -IPAddress 192.168.1.210

            ###########################

# Puis vérifier le Gestionnaire de serveur Windows

# En cas d'erreur post-déploiement concernant le DHCP, exécutez la commande suivante :

Set-ItemProperty -Path registry::HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\ServerManager\Roles\12 -Name ConfigurationState -Value 2

# Puis cliquer sur "Terminer la configuration DHCP" pour la terminer rapidement via l'interface graphique.

# Le serveur DHCP est prêt, il n'y a plus qu'à le configurer

