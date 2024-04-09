$Programacion1= New-ScheduledTaskTrigger -Weekly -WeeksInterval 1 -DaysOfWeek Monday -At 2:40pm

$User= «administrador»

$Accion1= New-ScheduledTaskAction -Execute «PowerShell.exe» -Argument «C:\Data\MonitorDiscosServidor.ps1»

Register-ScheduledTask -TaskName «MonitorDiscosServidor» -Trigger $Programacion1 -User $User -Action $Accion1 -RunLevel Highest –Force