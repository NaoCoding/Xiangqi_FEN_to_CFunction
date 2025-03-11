let last_board = null;

function convert(){

    last_board = null;  

    var fen = document.getElementById("fen").value;


    document.getElementById("code").value = "";

    for(var i=0;i<fen.split("\n").length;i++){
        if(last_board == null){
            last_board = FEN_parser(fen.split("\n")[i]);
            continue;
        }
        result = diff(last_board,FEN_parser(fen.split("\n")[i]))
        document.getElementById("code").value += `moveXiangqiRecord(board, ${result[0]}, ${result[1]}, ${result[2]}, ${result[3]});` + "\n";
        last_board = FEN_parser(fen.split("\n")[i])
    }
}

function FEN_parser(fen) {
    if (fen.split("/").length < 9) return null;

    try {
        return fen.split(" ")[0].split("/").map(row => {
            return row.split("").map(space => {
                return space.match(/\d/) ? " ".repeat(parseInt(space)) : space;
            }).join("");
        });
    } catch (error) {
        document.getElementById("code").value += "Invalid FEN string";
        return null;
    }
}

function diff(before, after) {
    let x1 = 0, y1 = 0, x2 = 0, y2 = 0;
    for (let i = 0; i < 10; i++) {
        for (let j = 0; j < 9; j++) {
            if (before[i][j] !== after[i][j]) {
                if (before[i][j] !== " " && after[i][j] === " ") {
                    x1 = 9 - i;
                    y1 = j;
                } else {
                    x2 = 9 - i;
                    y2 = j;
                }
            }
        }
    }
    return [x1, y1, x2, y2];
}


