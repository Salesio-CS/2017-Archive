package kif;

/**
*盤のポジションを扱うためのクラス
*/
public class Position {
    private int x;
    private int y;

    /**コンストラクタ
    * @param x 横座標
    * @param y 縦座標
    */
    public Position(int x,int y){
        this.x=x;
        this.y=y;
    }

    /** セットした横座標を取得 */
    public int getX(){
        return this.x;
    }
    /** セットした縦座標を取得 */
    public int getY(){
        return this.y;
    }
}
