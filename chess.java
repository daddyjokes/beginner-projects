import java.util.*;

public class Chess{

    String[][] board = new String[8][8];
    ArrayList<String> alive = new ArrayList<String>();

    static Scanner sc = new Scanner(System.in); 

    //Keeps a record of all moves
    ArrayList<String> history = new ArrayList<String>();

    //x,y for moving pieces around
    int start_x;
    int start_y;
    int end_x;
    int end_y;

    //0 = white's turn, 1 = black's turn
    int turn = 0;

    //Promotion coordinates; default pro_y = 1 (unreachable), pro_x = 0
    int pro_y = 1;
    int pro_x = 0;
    
    //Check if has castled
    boolean w_castle = true;
    boolean b_castle = true;



    //Declare pieces and set up board at beginning of game
    public void setUp(){

        /*
        UNICODE CHESS CHARACTERS
        White king      \u2654
        White queen     \u2655
        White rook      \u2656
        White bishop    \u2657
        White knight    \u2658
        White pawn      \u2659
        Black king      \u265A
        Black queen     \u265B
        Black rook      \u265C
        Black bishop    \u265D
        Black knight    \u265E
        Black pawn      \u265F
        */


        for (int y = 0; y < 8; y++){
            Arrays.fill(board[y], "-");
        }
        //White
        board[0][0] = "R";
        board[0][1] = "N";
        board[0][2] = "B";
        board[0][3] = "Q";
        board[0][4] = "K";
        board[0][5] = "B";
        board[0][6] = "N";
        board[0][7] = "R";
        board[1][0] = "P";
        board[1][1] = "P";
        board[1][2] = "P";
        board[1][3] = "P";
        board[1][4] = "P";
        board[1][5] = "P";
        board[1][6] = "P";
        board[1][7] = "P";
        //Black
        board[7][0] = "r";
        board[7][1] = "n";
        board[7][2] = "b";
        board[7][3] = "q";
        board[7][4] = "k";
        board[7][5] = "b";
        board[7][6] = "n";
        board[7][7] = "r";
        board[6][0] = "p";
        board[6][1] = "p";
        board[6][2] = "p";
        board[6][3] = "p";
        board[6][4] = "p";
        board[6][5] = "p";
        board[6][6] = "p";
        board[6][7] = "p";
    }



    //Print board with formatting and unicode chess symbols
    public void listPrint(){
        System.out.println();
        for (int y = 7; y >= 0; y--){
            System.out.print(y + 1);
            System.out.print("    ");
            for (int x = 0; x < 8; x++){
                if (board[y][x].equals("K")) System.out.print("\u2654  ");
                if (board[y][x].equals("Q")) System.out.print("\u2655  ");
                if (board[y][x].equals("R")) System.out.print("\u2656  ");
                if (board[y][x].equals("B")) System.out.print("\u2657  ");
                if (board[y][x].equals("N")) System.out.print("\u2658  ");
                if (board[y][x].equals("P")) System.out.print("\u2659  ");
                if (board[y][x].equals("k")) System.out.print("\u265A  ");
                if (board[y][x].equals("q")) System.out.print("\u265B  ");
                if (board[y][x].equals("r")) System.out.print("\u265C  ");
                if (board[y][x].equals("b")) System.out.print("\u265D  ");
                if (board[y][x].equals("n")) System.out.print("\u265E  ");
                if (board[y][x].equals("p")) System.out.print("\u265F  ");

                if (board[y][x].equals("-")) System.out.print("-- ");
            }
            System.out.println();
        }
        System.out.println("\n     a  b  c  d  e  f  g  h\n");
    }



    public boolean friendly_fire(String friendlies){
        if (board[end_y][end_x].matches(friendlies)) return true;
        else return false;
    }



    public void getAlive(){
        alive.clear();
        for (int y = 0; y < 8; y++){
            for (int x = 0; x < 8; x++){
                if (board[y][x] != "-"){
                    alive.add(board[y][x]);
                }
            }
        }
    }



    public void promotion(){
        pro_y = 1;
        pro_x = 0;

        for (int x = 0; x < 8; x++){

            //White
            if (board[7][x] == "P"){
                pro_y = 7;
                pro_x = x;
                break;
            }

            //Black
            if (board[0][x] == "p"){
                pro_y = 0;
                pro_x = x;
                break;
            }
        }
    }



    //Checks if piece's move matches piece's pattern, returns true if so
    public boolean pattern(){

        //Check if start_pos is empty
        if (board[start_y][start_x].matches("-")){
            return false;
        }

        //White
        if (turn == 0){

            //Check if piece is current player's piece
            if (board[start_y][start_x].matches("[KQRBNP]")){

                //Check if piece is attacking friendly piece
                if (friendly_fire("[KQRBNP]")) return false;
                else{

                    //Check if movement matches piece's movement pattern

                    //King
                    if (board[start_y][start_x].matches("K")){
                        if ((Math.abs(start_y - end_y) == 1) || (Math.abs(start_x - end_x) == 1)){
                            w_castle = false;
                            return true;
                        }

                        //Castle
                        else if ((w_castle == true) && (board[0][4] == "K")){
                            //Kingside
                            if (start_x + 2 == end_x){
                                if ((board[start_y][start_x + 1].matches("-")) && (board[start_y][start_x + 2].matches("-")) && (board[start_y][start_x + 3].matches("R"))){
                                    board[start_y][start_x + 1] = "R";
                                    board[start_y][start_x + 3] = "-";
                                    w_castle = false;
                                    return true;
                                }
                            }

                            //Queenside
                            if (start_x - 2 == end_x){
                                if ((board[start_y][start_x - 1].matches("-")) && (board[start_y][start_x - 2].matches("-")) && (board[start_y][start_x - 3].matches("-")) && (board[start_y][start_x - 4].matches("R"))){
                                    board[start_y][start_x - 1] = "R";
                                    board[start_y][start_x - 4] = "-";
                                    w_castle = false;
                                    return true;
                                }
                            }
                        }
                    }

                    //Queen
                    if (board[start_y][start_x].matches("Q")){

                        //Vertical
                        if ((start_y != end_y) && (start_x == end_x)){
                            
                            //Check if way is clear
                            for (int i = 1; i < Math.abs(start_y - end_y); i++){

                                //Move up
                                if (end_y - start_y > 0){
                                    if (board[start_y + i][start_x].matches("-"));
                                    else return false;
                                }

                                //Move down
                                else{
                                    if (board[start_y - i][start_x].matches("-"));
                                    else return false;
                                }
                            }
                            return true;
                        }

                        //Horizontal
                        if ((start_y == end_y) && (start_x != end_x)){

                            //Check if way is clear
                            for (int i = 1; i < Math.abs(start_x - end_x); i++){

                                //Move left
                                if (start_x - end_x > 0){
                                    if (board[start_y][start_x - i].matches("-"));
                                    else return false;
                                }

                                //Move right
                                else{
                                    if (board[start_y][start_x + i].matches("-"));
                                    else return false;
                                }
                            }
                            return true;
                        }

                        //Diagonal
                        if ((start_y != end_y) && (start_x != end_x) && (Math.abs(start_y - end_y) == Math.abs(start_x - end_x))){

                            //Check if way is clear
                            for (int i = 1; i < Math.abs(start_y - end_y); i++){

                                //Move Up
                                if (end_y - start_y > 0){

                                    //Move Up-Left
                                    if (start_x - end_x > 0){
                                        if (board[start_y + 1][start_x - i].matches("-"));
                                        else return false;
                                    }

                                    //Move Up-Right
                                    else{
                                        if (board[start_y + 1][start_x + i].matches("-"));
                                        else return false;
                                    }
                                }

                                //Move Down
                                else{

                                    //Move Down-Left
                                    if (start_x - end_x > 0){
                                        if (board[start_y - 1][start_x - i].matches("-"));
                                        else return false;
                                    }

                                    //Move Down-Right
                                    else{
                                        if (board[start_y - 1][start_x + i].matches("-"));
                                        else return false;
                                    }
                                }  
                            }
                            return true;
                        }
                    }

                    //Rook
                    if (board[start_y][start_x].matches("R")){

                        //Vertical
                        if ((start_y != end_y) && (start_x == end_x)){
                            
                            //Check if way is clear
                            for (int i = 1; i < Math.abs(start_y - end_y); i++){

                                //Move up
                                if (end_y - start_y > 0){
                                    if (board[start_y + i][start_x].matches("-"));
                                    else return false;
                                }

                                //Move down
                                else{
                                    if (board[start_y - i][start_x].matches("-"));
                                    else return false;
                                }
                            }
                            w_castle = false;
                            return true;
                        }

                        //Horizontal
                        if ((start_y == end_y) && (start_x != end_x)){

                            //Check if way is clear
                            for (int i = 1; i < Math.abs(start_x - end_x); i++){

                                //Move left
                                if (start_x - end_x > 0){
                                    if (board[start_y][start_x - i].matches("-"));
                                    else return false;
                                }

                                //Move right
                                else{
                                    if (board[start_y][start_x + i].matches("-"));
                                    else return false;
                                }
                            }
                            w_castle = false;
                            return true;
                        }
                    }

                    //Bishop
                    if (board[start_y][start_x].matches("B")){

                        if ((start_y != end_y) && (start_x != end_x) && (Math.abs(start_y - end_y) == Math.abs(start_x - end_x))){

                            //Check if way is clear
                            for (int i = 1; i < Math.abs(start_y - end_y); i++){

                                //Move Up
                                if (end_y - start_y > 0){

                                    //Move Up-Left
                                    if (start_x - end_x > 0){
                                        if (board[start_y + i][start_x - i].matches("-"));
                                        else return false;
                                    }

                                    //Move Up-Right
                                    else{
                                        if (board[start_y + i][start_x + i].matches("-"));
                                        else return false;
                                    }
                                }

                                //Move Down
                                else{

                                    //Move Down-Left
                                    if (start_x - end_x > 0){
                                        if (board[start_y - i][start_x - i].matches("-"));
                                        else return false;
                                    }

                                    //Move Down-Right
                                    else{
                                        if (board[start_y - i][start_x + i].matches("-"));
                                        else return false;
                                    }
                                }  
                            }
                            return true;
                        }
                        
                    }

                    //Knight
                    if (board[start_y][start_x].matches("N")){

                        //1 o'clock
                        if ((end_y - start_y == 2) && (end_x - start_x == 1)) return true;

                        //2 o'clock
                        else if ((end_y - start_y == 1) && (end_x - start_x == 2)) return true;

                        //4 o'clock
                        else if ((end_y - start_y == -1) && (end_x - start_x == 2)) return true;

                        //5 o'clock
                        else if ((end_y - start_y == -2) && (end_x - start_x == 1)) return true;

                        //7 o'clock
                        else if ((end_y - start_y == -2) && (end_x - start_x == -1)) return true;

                        //8 o'clock
                        else if ((end_y - start_y == -1) && (end_x - start_x == -2)) return true;

                        //10 o'clock
                        else if ((end_y - start_y == 1) && (end_x - start_x == -2)) return true;

                        //11 o'clock
                        else if ((end_y - start_y == 2) && (end_x - start_x == -1)) return true;
                    }

                    //Pawn
                    if (board[start_y][start_x].matches("P")){

                        //If Attack
                        if ((Math.abs(start_x - end_x) == 1) && (end_y - start_y == 1) && (board[end_y][end_x].matches("[kqrbnp]"))) return true;
                        
                        //If Move
                        else if ((start_y < end_y) && (board[end_y][end_x].matches("-")) && (start_x == end_x)){

                            //If pawn has not moved
                            if (start_y == 1){
                                if ((end_y - start_y == 2) || (end_y - start_y == 1)){
                                    return true;
                                }
                            }

                            //If pawn has moved
                            else{
                                if ((end_y - start_y == 1)){
                                    return true;
                                }
                            }
                        }
                    }
                }
            }
        }

        //Black
        else if (turn == 1){

            //Check if piece is current player's piece
            if (board[start_y][start_x].matches("[kqrbnp]")){

                //Check if piece is attacking friendly piece
                if (friendly_fire("[kqrbnp]")) return false;
                else{

                    //King
                    if (board[start_y][start_x].matches("k")){
                        if ((Math.abs(start_y - end_y) == 1) || (Math.abs(start_x - end_x) == 1)){
                            b_castle = false;
                            return true;
                        }

                        //Castle
                        else if ((b_castle == true) && (board[0][4] == "k")){
                            //Kingside
                            if (start_x + 2 == end_x){
                                if ((board[start_y][start_x + 1].matches("-")) && (board[start_y][start_x + 2].matches("-")) && (board[start_y][start_x + 3].matches("r"))){
                                    board[start_y][start_x + 1] = "r";
                                    board[start_y][start_x + 3] = "-";
                                    b_castle = false;
                                    return true;
                                }
                            }

                            //Queenside
                            if (start_x - 2 == end_x){
                                if ((board[start_y][start_x - 1].matches("-")) && (board[start_y][start_x - 2].matches("-")) && (board[start_y][start_x - 3].matches("-")) && (board[start_y][start_x - 4].matches("r"))){
                                    board[start_y][start_x - 1] = "r";
                                    board[start_y][start_x - 4] = "-";
                                    b_castle = false;
                                    return true;
                                }
                            }
                        }
                    }

                    //Queen
                    if (board[start_y][start_x].matches("q")){

                        //Vertical
                        if ((start_y != end_y) && (start_x == end_x)){
                            
                            //Check if way is clear
                            for (int i = 1; i < Math.abs(start_y - end_y); i++){

                                //Move up
                                if (end_y - start_y > 0){
                                    if (board[start_y + i][start_x].matches("-"));
                                    else return false;
                                }

                                //Move down
                                else{
                                    if (board[start_y - i][start_x].matches("-"));
                                    else return false;
                                }
                            }
                            return true;
                        }

                        //Horizontal
                        if ((start_y == end_y) && (start_x != end_x)){

                            //Check if way is clear
                            for (int i = 1; i < Math.abs(start_x - end_x); i++){

                                //Move left
                                if (start_x - end_x > 0){
                                    if (board[start_y][start_x - i].matches("-"));
                                    else return false;
                                }

                                //Move right
                                else{
                                    if (board[start_y][start_x + i].matches("-"));
                                    else return false;
                                }
                            }
                            return true;
                        }

                        //Diagonal
                        if ((start_y != end_y) && (start_x != end_x) && (Math.abs(start_y - end_y) == Math.abs(start_x - end_x))){

                            //Check if way is clear
                            for (int i = 1; i < Math.abs(start_y - end_y); i++){

                                //Move Up
                                if (end_y - start_y > 0){

                                    //Move Up-Left
                                    if (start_x - end_x > 0){
                                        if (board[start_y + 1][start_x - i].matches("-"));
                                        else return false;
                                    }

                                    //Move Up-Right
                                    else{
                                        if (board[start_y + 1][start_x + i].matches("-"));
                                        else return false;
                                    }
                                }

                                //Move Down
                                else{

                                    //Move Down-Left
                                    if (start_x - end_x > 0){
                                        if (board[start_y - 1][start_x - i].matches("-"));
                                        else return false;
                                    }

                                    //Move Down-Right
                                    else{
                                        if (board[start_y - 1][start_x + i].matches("-"));
                                        else return false;
                                    }
                                }  
                            }
                            return true;
                        }
                    }

                    //Rook
                    if (board[start_y][start_x].matches("r")){

                        //Vertical
                        if ((start_y != end_y) && (start_x == end_x)){
                            
                            //Check if way is clear
                            for (int i = 1; i < Math.abs(start_y - end_y); i++){

                                //Move up
                                if (end_y - start_y > 0){
                                    if (board[start_y + i][start_x].matches("-"));
                                    else return false;
                                }

                                //Move down
                                else{
                                    if (board[start_y - i][start_x].matches("-"));
                                    else return false;
                                }
                            }
                            b_castle = false;
                            return true;
                        }

                        //Horizontal
                        if ((start_y == end_y) && (start_x != end_x)){

                            //Check if way is clear
                            for (int i = 1; i < Math.abs(start_x - end_x); i++){

                                //Move left
                                if (start_x - end_x > 0){
                                    if (board[start_y][start_x - i].matches("-"));
                                    else return false;
                                }

                                //Move right
                                else{
                                    if (board[start_y][start_x + i].matches("-"));
                                    else return false;
                                }
                            }
                            b_castle = false;
                            return true;
                        }
                    }

                    //Bishop
                    if (board[start_y][start_x].matches("b")){

                        if ((start_y != end_y) && (start_x != end_x) && (Math.abs(start_y - end_y) == Math.abs(start_x - end_x))){

                            //Check if way is clear
                            for (int i = 1; i < Math.abs(start_y - end_y); i++){

                                //Move Up
                                if (end_y - start_y > 0){

                                    //Move Up-Left
                                    if (start_x - end_x > 0){
                                        if (board[start_y + i][start_x - i].matches("-"));
                                        else return false;
                                    }

                                    //Move Up-Right
                                    else{
                                        if (board[start_y + i][start_x + i].matches("-"));
                                        else return false;
                                    }
                                }

                                //Move Down
                                else{

                                    //Move Down-Left
                                    if (start_x - end_x > 0){
                                        if (board[start_y - i][start_x - i].matches("-"));
                                        else return false;
                                    }

                                    //Move Down-Right
                                    else{
                                        if (board[start_y - i][start_x + i].matches("-"));
                                        else return false;
                                    }
                                }  
                            }
                            return true;
                        }
                        
                    }

                    //Knight
                    if (board[start_y][start_x].matches("n")){

                        //1 o'clock
                        if ((end_y - start_y == 2) && (end_x - start_x == 1)) return true;

                        //2 o'clock
                        else if ((end_y - start_y == 1) && (end_x - start_x == 2)) return true;

                        //4 o'clock
                        else if ((end_y - start_y == -1) && (end_x - start_x == 2)) return true;

                        //5 o'clock
                        else if ((end_y - start_y == -2) && (end_x - start_x == 1)) return true;

                        //7 o'clock
                        else if ((end_y - start_y == -2) && (end_x - start_x == -1)) return true;

                        //8 o'clock
                        else if ((end_y - start_y == -1) && (end_x - start_x == -2)) return true;

                        //10 o'clock
                        else if ((end_y - start_y == 1) && (end_x - start_x == -2)) return true;

                        //11 o'clock
                        else if ((end_y - start_y == 2) && (end_x - start_x == -1)) return true;
                    }

                    //Pawn
                    if (board[start_y][start_x].matches("p")){

                        //If Attack
                        if ((Math.abs(start_x - end_x) == 1) && (start_y - end_y == 1) && (board[end_y][end_x].matches("[KQRBNP]"))) return true;
                        
                        //If Move
                        else if ((start_y > end_y) && (board[end_y][end_x].matches("-")) && (start_x == end_x)){

                            //If pawn has not moved
                            if (start_y == 6){
                                if ((end_y - start_y == -2) || (end_y - start_y == -1)){
                                    return true;
                                }
                            }

                            //If pawn has moved
                            else{
                                if ((end_y - start_y == -1)){
                                    return true;
                                }
                            }
                        }
                    }
                }
            }
        }
        return false;
    }



    //Uses pattern() to check if move is legal, then makes the move
    public void move(String start, String end){

        //Start to blank area (--)

        //User-side commands to lower-level x,y integers for board[x][y]
        //Char to x integer
        if ((String.valueOf(start.charAt(0))).matches("a")) start_x = 0;
        if ((String.valueOf(start.charAt(0))).matches("b")) start_x = 1;
        if ((String.valueOf(start.charAt(0))).matches("c")) start_x = 2;
        if ((String.valueOf(start.charAt(0))).matches("d")) start_x = 3;
        if ((String.valueOf(start.charAt(0))).matches("e")) start_x = 4;
        if ((String.valueOf(start.charAt(0))).matches("f")) start_x = 5;
        if ((String.valueOf(start.charAt(0))).matches("g")) start_x = 6;
        if ((String.valueOf(start.charAt(0))).matches("h")) start_x = 7;
        //Char to y integer
        start_y = Integer.parseInt(start.charAt(1) + "") - 1;


        //End to piece

        //User-side commands to lower-level x,y integers for board[x][y]
        //Char to x integer
        if ((String.valueOf(end.charAt(0))).matches("a")) end_x = 0;
        if ((String.valueOf(end.charAt(0))).matches("b")) end_x = 1;
        if ((String.valueOf(end.charAt(0))).matches("c")) end_x = 2;
        if ((String.valueOf(end.charAt(0))).matches("d")) end_x = 3;
        if ((String.valueOf(end.charAt(0))).matches("e")) end_x = 4;
        if ((String.valueOf(end.charAt(0))).matches("f")) end_x = 5;
        if ((String.valueOf(end.charAt(0))).matches("g")) end_x = 6;
        if ((String.valueOf(end.charAt(0))).matches("h")) end_x = 7;
        //Char to y integer
        end_y = Integer.parseInt(end.charAt(1) + "") - 1;


        if (pattern()){

            //If movement matches piece's movement pattern (move legal)
            String piece = board[start_y][start_x];
            board[start_y][start_x] = "-";
            board[end_y][end_x] = piece;
            listPrint();

            //Switch player
            if (turn == 0) turn = 1;
            else if (turn == 1) turn = 0;
        }
    }



    /*En passant not added; can to made by temporarily saving pos when
    pawn moved 2 spaces; then create fake, temporarily pawn at space behind
    which does not display but is targetable*/
    public static void main(String[] args){
        Chess game = new Chess();

        System.out.println("Java Chess 1.0. Created by Devin Zhang. 9/10/19 - 9/17/19.\nMovement format: 'start_pos end_pos', ex 'e2 e4'");

        game.setUp();
        game.listPrint();
        
        while (true){

            game.promotion();

            String input = sc.nextLine();

            //Promotion
            if (game.pro_y != 1){
                
                //White
                if (game.pro_y == 7){
                    if (input.matches("[QRBN]")){
                        game.board[game.pro_y][game.pro_x] = input;
                        game.listPrint();
                    }
                }

                //Black
                if (game.pro_y == 0){
                    if (input.matches("[qrbn]")){
                        game.board[game.pro_y][game.pro_x] = input;
                        game.listPrint();
                    }
                }
            }

            //No promotion eligible
            else{

                //Format input
                if (input.length() >= 5){
                    input = input.substring(0,5);
                    if ((String.valueOf(input.charAt(0))).matches("[a-h]")){
                        if ((String.valueOf(input.charAt(1))).matches("[1-8]")){
                            if ((String.valueOf(input.charAt(2))).matches(" ")){
                                if ((String.valueOf(input.charAt(3))).matches("[a-h]")){
                                    if ((String.valueOf(input.charAt(4))).matches("[1-8]")){
                                        String formal_input[] = input.split(" ");

                                        if (formal_input[0] != formal_input[1]){

                                            //Check if input is legal, then move piece
                                            game.move(formal_input[0], formal_input[1]);

                                            game.history.add(input);

                                            //Check if King is dead
                                            game.getAlive();
                                            if (game.alive.contains("K"));
                                            else{
                                                System.out.println("Game Over: Black Wins!");
                                                System.out.println(game.history.toString().replace("[", "").replace("]", ""));
                                                break;
                                            }
                                            if (game.alive.contains("k"));
                                            else{
                                                System.out.println("Game Over: White Wins!");
                                                System.out.println(game.history.toString().replace("[", "").replace("]", ""));
                                                break;
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }
}