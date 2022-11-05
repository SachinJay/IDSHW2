$TargetFolders = Get-Content input.txt
$AuditUser = "Everyone"
$AuditRules = "Delete,DeleteSubdirectoriesAndFiles,ChangePermissions,Takeownership,CreateFiles,AppendData,ExecuteFile,ReadData"
$InheritType = "ContainerInherit,ObjectInherit"
$AuditType = "Success"
$AccessRule = New-Object System.Security.AccessControl.FileSystemAuditRule($AuditUser,$AuditRules,$InheritType,"None",$AuditType)
foreach ($TargetFolder in $TargetFolders)
{
    $ACL = Get-Acl $TargetFolder
    $ACL.SetAuditRule($AccessRule)
    Write-Host "Processing >",$TargetFolder
    $ACL | Set-Acl $TargetFolder
}
Write-Host "Audit Policy applied successfully."
