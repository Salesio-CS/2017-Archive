package kif;

import java.util.*;

import kif.Piece;

/**
*盤状にどの駒があるかを管理するクラス
*/
public class Board {
    /** 平手の時の初期局面(駒のid)
    * [0][],[][0],[10][],[][10]は使用しない
    */
    public static final int[][] _board ={
        {00,00,00,00,00,00,00,00,00,00,00},
        {00,-2,-3,-4,-5,-8,-5,-4,-3,-2,00},
        {00, 0,-7, 0, 0, 0, 0, 0,-6, 0,00},
        {00,-1,-1,-1,-1,-1,-1,-1,-1,-1,00},
        {00, 0, 0, 0, 0, 0, 0, 0, 0, 0,00},
        {00, 0, 0, 0, 0, 0, 0, 0, 0, 0,00},
        {00, 0, 0, 0, 0, 0, 0, 0, 0, 0,00},
        {00, 1, 1, 1, 1, 1, 1, 1, 1, 1,00},
        {00, 0, 6, 0, 0, 0, 0, 0, 7, 0,00},
        {00, 2, 3, 4, 5, 8, 5, 4, 3, 2,00},
        {00,00,00,00,00,00,00,00,00,00,00}
    };

    /** 現在の盤面を保持する配列 */
    private kif.Piece[][] board;

    /** 先手の持ち駒 */
    private kif.Caputure sente=new Caputure();
    /** 後手の持ち駒 */
    private kif.Caputure gote=new Caputure();

    /** コンストラクタ */
    public Board(){
        this.init(_board);
    }

    /**コマ落ちの場合のコンストラクタ
    @param board コマ落ちのどういう局面であるか
    */
    public Board(final int[][] board){
        this.init(board);
    }

    /**先手の持ち駒を取得する
    * @return 先手の持ち駒
    */
    public kif.Caputure getSenteCapture(){
        return this.sente;
    }
    /**後手の持ち駒を取得する
    * @return 後手の持ち駒
    */
    public kif.Caputure getGoteCapture(){
        return this.gote;
    }

    //TODO:ここに落とす駒の位置だけを格納した配列で処理するコンストラクタをかく．

    /** 初期化処理 */
    private void init(final int[][] b){
        this.board=new kif.Piece[b.length][b[0].length];
        //TODO:n枚落ちの場合の処理をかく
        for (int i = 0; i < b.length; ++i) {
            for(int j = 0; j < b.length; ++j){
                if(b[i][j]==0||i==0||j==0||i==10||j==10){
                    this.board[i][j]=new kif.Piece(kif.Piece.Type.NU, kif.Piece.Turn.NONE);
                }else{
                    this.board[i][j]=new kif.Piece(kif.Piece.getType(b[i][j]), kif.Piece.getTurn(b[i][j]));
                }
            }
        }
    }

    /**座標クラスを使って盤状の駒のidを取ってくる
    * @param p 取ってくる座標
    * @return 取ってきた駒のid
    */
    public int getPieceIdByPosition(kif.Position p){
        return this.getPieceByPosition(p).getPieceId();
    }


    /**座標クラスを使って盤状の駒を取ってくる
    * @param p 取ってくる座標
    * @return 取ってきた駒のid
    */
    public kif.Piece getPieceByPosition(kif.Position p){
        return this.board[p.getY()][10 - p.getX()];
    }

    /**座標クラスを使って盤状の駒を上書きする
    * @param pos 変更する座標
    * @param piece この駒で上書きする
    */
    protected void setPieceByPosition(kif.Position pos,kif.Piece piece){
        this.board[pos.getY()][10 - pos.getX()]=piece;
    }

    /**座標クラスを使って盤状の駒を削除する
    * @param pos 削除する座標
    */
    protected void deletePieceByPosition(kif.Position pos){
        this.board[pos.getY()][10 - pos.getX()]=new kif.Piece(kif.Piece.Type.NU, kif.Piece.Turn.NONE);
    }



    /**盤面を文字列で返す
    *@return 盤を表現した文字列
    */
    public String getBoardString(){
        String s="";
        for(int i = 1;i <= 9; i++){
            for(int j = 10; j > 0; j--){
                if(j == 10){
                    s += String.format("P%d", i);
                }else{
                    s += String.format("%3s", board[i][10 - j].getPieceString());
                }
            }
            s+="\n";
        }
        return s;
    }


    /** 盤面をコンソールに表示する */
    public void showBoardToConsole(){
        int[] cap;
        cap = gote.getCapture();
        System.out.println("後手持ち駒：");
        for(int i = 1; i < cap.length; i++){
            System.out.print(String.format("%s:%d,", kif.Piece.getType(i).getString(), cap[i]));
        }
        System.out.println();
        /*
        for(int i = 0;i <= 9; i++){
            for(int j = 10; j > 0; j--){
                if(j == 10){
                    System.out.print(String.format("%2d:",i));
                }else if(i == 0){
                    System.out.print(String.format("%2d ",j));
                }else{
                    System.out.print(String.format("%2s,",board[i][10 - j].getPieceType().getString()));
                }
            }
            System.out.println();
        }
        */
        System.out.println(this.getBoardString());
        cap = sente.getCapture();
        System.out.println("先手持ち駒：");
        for(int i = 1; i < cap.length; i++){
            System.out.print(String.format("%s:%d,", kif.Piece.getType(i).getString(), cap[i]));
        }
        System.out.println();
    }


    /** 駒の移動を行う
    * @param p 手番
    * @return 移動した駒のid 移動に失敗したら"0"
    */
    public int movePieceInBoard(kif.Phase p){
        // 移動した駒のid
        int fromPieceId=getPieceIdByPosition(p.getBefore());
        int toPieceId=getPieceIdByPosition(p.getAfter());

        System.out.println("from: " + fromPieceId + ", to: " + toPieceId);

        if(fromPieceId == 0){
            //移動前の座標に何も駒がなければ失敗
            return 0;
        }

        if(toPieceId != 0){
            //移動先の座標に何か駒がある場合
            System.out.println("fromPieceId * toPieceId:"+fromPieceId * toPieceId);
            if(fromPieceId * toPieceId > 0){
                //同じ手番の駒であれば失敗
                return 0;
            }else{
                //違う手番の駒であればその駒を持ち手に入れる
                if(p.isSente()){
                    this.sente.add(toPieceId);
                }else{
                    this.gote.add(toPieceId);
                }
            }
        }

        //上書き
        setPieceByPosition(p.getToPosition(),p.getPiece());
        deletePieceByPosition(p.getFromPosition());

        return fromPieceId;
    }

    /** 駒を打つ
    * @param p 手番
    * @return 打った駒のid 移動に失敗したら"0"
    */
    public int putPiece(kif.Phase p){
        int toPieceId=getPieceIdByPosition(p.getAfter());
        if(toPieceId != 0){
            //打つところに何かしらの駒があれば失敗
            return 0;
        }
        //上書き
        setPieceByPosition(p.getToPosition(),p.getPiece());
        //駒を使用
        if(p.getPiece().isSente()){
            this.sente.use(p.getPiece());
        }else{
            this.gote.use(p.getPiece());
        }
        return getPieceIdByPosition(p.getAfter());
    }

}
