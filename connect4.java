import java.util.Scanner;

public class Connect4{

    public int[][] board;
    public int width = 7;
    public int height = 6;
    public Scanner scanner;
    public int playerTurn = 2;
    public boolean running = true;


    //Runs first
    public void createBoard(){
        board = new int [height][width];
        scanner = new Scanner(System.in);

        for (int y = 0; y < height; y++){
            for (int x = 0; x < width; x++){
                board[y][x] = 0;
            }
        }
    }


    //Stylised for better user interface
    public void displayBoard(){
        for (int y = 0; y < height; y++){
            String line = "";

            for (int x = 0; x < width; x++){
                if (board[y][x] == 0) line += " _ ";
                else line += " " + board[y][x] + " ";
            }
            System.out.println(line);
        }
    }


    public void addPiece(int index, int player){
        if (index > 7){
            index = 7;
        }
        if (index < 1){
            index = 1;
        }

        //Convert natural numbers to 0-based
        index--;

        //Backwards For loop, start from top going down
        for (int i = height - 1; i > -1; i--){
            if (board[i][index] == 0){
                board[i][index] = player;
                break;
            }
        }
    }


    public void checkInput(){
        String input = scanner.nextLine();
        if (input.equals("")){
            running = false;
            return;
        }

        //User input string to int
        int num = Integer.parseInt(input);
        if (playerTurn == 1) playerTurn = 2;
        else playerTurn = 1;

        addPiece(num, playerTurn);
        displayBoard();
        checkWinner();
    }


    public int checkWinner(){
        boolean won = false;
        int winner = 0;

        if (winner != 0){
            System.out.println("Winner: " + winner);
        }

        for (int i = 0; i < 3; i++){
            for (int y = 0; y < height; y++){
                for (int x = 0; x < width; x++){
                    if (board[y][x] == 0) continue;

                    boolean horizontal = false;
                    if (width - x >= 4){
                        horizontal = true;
                        for (int j = 0; j < 4; j++){
                            if (board[y][x + j] != i){
                                horizontal = false;
                                break;
                            }
                        }
                    }

                    boolean vertical = false;
                    if (height - y >= 4){
                        vertical = true;
                        for (int j = 0; j < 4; j++){
                            if (board[y + j][x] != i){
                                vertical = false;
                                break;
                            }
                        }
                    }
                    
                    boolean diagonal_left = false;
                    if (height - y >= 4 && x - 4 > -1){
                        diagonal_left = true;
                        for (int j = 0; j < 4; j++){
                            if (board[y + j][x - j] != i){
                                diagonal_left = false;
                                break;
                            }
                        }
                    }
                    
                    boolean diagonal_right = false;
                    if (height - y >= 4 && x + 4 < width){
                        diagonal_right = true;
                        for (int j = 0; j < 4; j++){
                            if (board[y + j][x + j] != i){
                                diagonal_right = false;
                                break;
                            }
                        }
                    }
                    
                    won = horizontal||vertical||diagonal_left||diagonal_right;
                    if (won){
                        winner = i;
                    }
                    return winner;
                }
            }
        }
        return 0;
    }


    public static void main(String[] args){

        Connect4 game = new Connect4();
        game.createBoard();
        while (game.running){
            game.checkInput();
        }
    }
}