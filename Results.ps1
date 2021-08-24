[int] $FIRST_NUM = Read-Host - Prompt 'Input a Number'
[int] $SECOND_NUM = Read-Host - Prompt 'Input a second Number'
$SUM = $FIRST_NUM + $SECOND_NUM
$SUB = $FIRST_NUM - $SECOND_NUM
$SMUL = $FIRST_NUM * $SECOND_NUM
$DIV = $FIRST_NUM / $SECOND_NUM
Write-Host $FIRST_NUM "+" $SECOND_NUM "=" $SUM
Write-Host $SUM

Write-Host $FIRST_NUM "-" $SECOND_NUM "=" $SUB
Write-Host $SUB

Write-Host $FIRST_NUM "*" $SECOND_NUM "=" $SMUL
Write-Host $SMUL

Write-Host $FIRST_NUM "/" $SECOND_NUM "=" $DIV
Write-Host $DIV

Write-Host "Testing 1,2,3"