export function GetObj(objName) {
    if(document.getElementById){
        return eval('document.getElementById("'+objName+'")')
    }
    else{
        return eval('document.all.'+objName)
    }
}
