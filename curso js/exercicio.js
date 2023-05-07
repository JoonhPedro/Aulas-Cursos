function calcMédia(notas) {
    let notas1 = notas[0]
    let notas2 = notas[1]
    let notas3 = notas[2]
    let media = (notas1 + notas2 + notas3)/3;
    if(media>=7 && notas1>3 && notas2>3 && notas3>3){
      console.log("parabens você foi Aprovado");
    }else {
      console.log ("infelizmente você nao foi Aprovado");
    }
  }
  calcMédia([8,7,10]);