package kif;

import java.awt.*;
import java.awt.event.*;
import javax.swing.*;
import java.io.*;
import java.util.*;
import javax.swing.filechooser.*;


/** メインフレーム */
public class Kif extends JFrame {
    private static final long serialVersionUID = 1L;


    /** メインパネル */
    private JPanel contentPane = new JPanel();
    private BorderLayout borderLayout1 = new BorderLayout();
    /** テキストフィールド */
    private JTextField text = new JTextField("");
    /** 今何手目？ */
    private int n=1;
    /** 状態とか */
    private int state=0;
    /** CSAファイル書き込み用 */
    private Files files;
    /** 盤面 */
    private kif.Board board;
    /** ボタン */
    private ArrayList<ArrayList<PositionButton>> boardButtons;
    /** 手番保存用のバッファ */
    private kif.Position positionBuffer;
    /** 駒打ち用のバッファ */
    private kif.Piece pieceBuffer;
    /** 先手の駒台 */
    private CaputureTable senteTable;
    /** 後手の駒台 */
    private CaputureTable goteTable;
    /** CSA保存用 */
    private kif.CsaData csa;

    /** 駒台と将棋盤のボタン群を配置するパネル
    * 内訳
    *  0 ...  17:後手の駒台
    * 18 ...  98:将棋盤
    * 99 ... 108:先手の駒台
    */
    private JPanel keyPanel;


    /** フレームのビルド */
    public Kif() {
        this.contentPane.setLayout(borderLayout1);
        this.setSize(new Dimension(720, 960));
        this.setTitle("棋譜作るよ:"+n+"手目");
        this.setContentPane(contentPane);
        this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        //テキストフィールドを配置
        contentPane.add(text, BorderLayout.NORTH);
        //ボタンを配置するパネルを用意
        this.keyPanel = new JPanel();
        this.keyPanel.setLayout(new GridLayout(13, 9));

        /** 盤を初期化 */
        this.board = new kif.Board();
        /** データを初期化 */
        this.csa= new kif.CsaData("","","");
        /** 先手の駒台を初期化 */
        this.senteTable = new CaputureTable(this.board.getSenteCapture(), kif.Piece.Turn.SENTE);
        /** 後手の駒台を初期化 */
        this.goteTable = new CaputureTable(this.board.getGoteCapture(), kif.Piece.Turn.SENTE);

        //後手の駒台を設置
        for (int i = 0; i < 18; i++) {
            if(Math.abs(i % 9 - 4) >= 4){
                this.keyPanel.add(new JPanel(), i);
            }else if(i < 9){
                this.keyPanel.add(this.goteTable.getLabels(i - 1), i);
            }else{
                this.keyPanel.add(this.goteTable.getButtons(i - 10), i);
            }
        }

        //将棋盤を設置
        this.contentPane.add(keyPanel, BorderLayout.CENTER);
        //ボタンをレイアウトにはめこんでいく（81個）
        this.boardButtons=new ArrayList<>();
        for(int i=1; i<=9;i++){
            this.boardButtons.add(new ArrayList<>());
            for(int j=9;j>0;j--){
                this.boardButtons.get(i-1).add(new PositionButton(new kif.Position(j, i)));
                this.keyPanel.add(boardButtons.get(i - 1).get(9 - j), (9 - j) + 9 * (i - 1) + 18);
            }
        }

        //先手の駒台を設置
        for (int i = 0; i < 18; i++) {
            if(Math.abs(i % 9 - 4) >= 4){
                this.keyPanel.add(new JPanel(), i+99);
            }else if(i < 9){
                this.keyPanel.add(this.senteTable.getLabels(i - 1), i + 99);
            }else{
                this.keyPanel.add(this.senteTable.getButtons(i - 10), i + 99);
            }
        }

        //将棋盤のテキストを反映
        updatePositionButtonText();

        //次の一手と保存ボタン
        JPanel bottomPanel = new JPanel();
        //ボタンを配置するパネルを用意
        bottomPanel.add(new WriteButton(this),BorderLayout.WEST);
        contentPane.add(bottomPanel, BorderLayout.SOUTH);
        this.setVisible(true);

    }

    /** テキストフィールドに引数の文字列を入れる
    * @param c 任意の文字列
    */
    public void set(String c) {
        text.setText(c);
    }

    /** 情報の入力を終了してcsaファイルへ書き込む */
    protected void saveCSA(){
        JFileChooser filechooser = new JFileChooser();
        filechooser.setFileFilter(new FileNameExtensionFilter("*.csa", "csa"));
        int selected = filechooser.showSaveDialog(this);
        if (selected == JFileChooser.APPROVE_OPTION){
            try{
                File file = filechooser.getSelectedFile();
                PrintWriter pw = new PrintWriter(new BufferedWriter(new FileWriter(file)));
                pw.println(this.csa.getCSAString());
                pw.close();
                //final String fullpath = filechooser.getDirectory() + filechooser.getFile();
                System.out.println(file.getName());
                System.out.println(file.getPath());
                System.out.println(this.csa.getCSAString());
            }catch(IOException e){
                System.out.println(e);
            }


        }else if (selected == JFileChooser.CANCEL_OPTION){
            System.out.println("キャンセルされました");
        }else if (selected == JFileChooser.ERROR_OPTION){
            System.out.println("エラー又は取消しがありました");
        }
        //System.out.println(this.csa.getCSAString());
    }

    /** 座標クラスから座標ボタンを取得する */
    protected PositionButton getPositionButtonByPosition(kif.Position p){
        return boardButtons.get(p.getY()).get(p.getX());
    }

    /** 座標ボタンのテキストを更新する */
    protected void updatePositionButtonText(){
        for(int i = 1; i <= 9;i++){
            for(int j = 9; j > 0;j--){
                PositionButton b = boardButtons.get(i-1).get(9-j);
                String buf = board.getPieceByPosition(new kif.Position(j,i)).getPieceString_ja();
                b.setText(buf.equals(" * ") ? "" : buf);
            }
        }
    }

    /** 駒台のテキストを更新する */
    protected void updateCaptureTabelText(){
        for (int i = 0; i < 7; i++) {
            this.senteTable.getButtons(i).update();
            this.goteTable.getButtons(i).update();
        }
    }

    /** 座標を入力するボタン */
    public class PositionButton extends JButton implements ActionListener {
        private static final long serialVersionUID = 1L;
        private kif.Position pos;

        public PositionButton(kif.Position p) {
            super();
            this.pos=p;
            this.addActionListener(this);
        }

        public void actionPerformed(ActionEvent e) {
            String keyNumber = "" + this.pos.getX() + "" + this.pos.getY();
            System.out.println("event:(" + this.pos.getX() + "," + this.pos.getY() + ") = " + board.getPieceByPosition(this.pos).getPieceType().getString());
            switch (state) {
            case 0:
                positionBuffer=new kif.Position(this.pos.getX(),this.pos.getY());
                set(String.format("移動前座標:%2s 移動先の座標をクリックしてください ",keyNumber));
                state++;
                break;
            case 1:
                kif.Phase t=new kif.Phase(positionBuffer, this.pos, board.getPieceByPosition(positionBuffer), 1);;
                state--;
                if(positionBuffer.getX() == 0 && positionBuffer.getY() == 0){
                    //駒打
                    t=new kif.Phase(positionBuffer, this.pos, pieceBuffer, 1);
                    if (board.putPiece(t) != 0) {
                        n++;
                        board.showBoardToConsole();
                        updatePositionButtonText();
                        updateCaptureTabelText();
                    }else {
                        set("駒打ちに失敗しました．もう一度移動前座標入力からやり直してください");
                        System.out.println("駒打ち失敗");
                        break;
                    }
                }else if(board.movePieceInBoard(t) != 0 ){
                    n++;
                    board.showBoardToConsole();
                    //成れるか判定して成れるんだったらダイアログできく
                    if(t.canPromote()){
                        int option = JOptionPane.showConfirmDialog(this, "成りますか？");
                        if (option == JOptionPane.YES_OPTION){
                            t.getPiece().promote();
                        }
                    }
                    updatePositionButtonText();
                    updateCaptureTabelText();
                }else{
                    set("駒の移動に失敗しました．もう一度移動前座標入力からやり直してください");
                    System.out.println("移動失敗");
                    break;
                }
                System.out.println(t.getString());
                set(String.format("%s 次の手の移動前座標をクリックしてください", t.getString()));
                csa.addPhaseLog(t);
                break;
            default:
            }
        }
    }

    /** 保存ボタン */
    public class WriteButton extends JButton implements ActionListener {
        private static final long serialVersionUID = 1L;

        public WriteButton(Kif k) {
            super("棋譜を保存");
            this.addActionListener(this);
        }

        public void actionPerformed(ActionEvent e) {
            saveCSA();
        }
    }

    /** 駒台を表現するボタンとラベルのまとめ */
    public class CaputureTable {

        /** 駒台用のボタンをまとめておくリスト */
        private ArrayList<CaptureButton> caputureButtons;
        /** 駒台用のラベルをまとめておくリスト */
        private ArrayList<JLabel> caputureLabels;
        /** 持ち駒 */
        private kif.Caputure caputure;
        /** 先手か後手か */
        private kif.Piece.Turn turn;

        public CaputureTable(kif.Caputure c,kif.Piece.Turn t){
            this.caputure = c;
            this.turn = t;
            this.caputureButtons = new ArrayList<>();
            this.caputureLabels = new ArrayList<>();
            for(int i = 1; i < c.getCapture().length; i++){
                this.caputureButtons.add(new CaptureButton(i));
                this.caputureLabels.add(new JLabel(kif.Piece.getType(i).getString_ja()));
            }
        }

        /** 駒台用のボタンをまとめておくリストを取得
        *@return 駒台用のボタンをまとめておくリスト
        */
        public ArrayList<CaptureButton> getButtons(){
            return this.caputureButtons;
        }

        /** 駒台用のラベルをまとめておくリストを取得
        *@return 駒台用のラベルをまとめておくリスト
        */
        public ArrayList<JLabel> getLabels(){
            return this.caputureLabels;
        }

        /** 駒台用のボタンを取得
        *@param i インデックス
        *@return 駒台用のボタン
        */
        public CaptureButton getButtons(int i){
            return this.caputureButtons.get(i);
        }

        /** 駒台用のラベルを取得
        *@param i インデックス
        *@return 駒台用のラベル
        */
        public JLabel getLabels(int i){
            return this.caputureLabels.get(i);
        }

        /** 駒台用のボタン */
        public class CaptureButton extends JButton implements ActionListener {
            /** どの駒のボタンであるか */
            private int id;
            public CaptureButton(int i){
                super(String.format("残り: %d", caputure.getCapture(i)));
                this.id = i;
                this.addActionListener(this);
            }

            /** 持ち駒の個数表示テキストを更新 */
            public void update(){
                this.setText(String.format("残り: %d", caputure.getCapture(this.id)));
            }

            public void actionPerformed(ActionEvent e) {
                switch(state){
                    case 0:
                        if (caputure.getCapture(id) > 0) {
                            positionBuffer=new kif.Position(0,0);
                            set(String.format("移動前座標:駒台 駒:%s 移動先の座標をクリックしてください", kif.Piece.getType(this.id).getString_ja()));
                            pieceBuffer = new kif.Piece(kif.Piece.getType(this.id), turn);
                            state++;
                        }else {
                            set("その駒は持っていません もう一度移動前座標入力からやり直してください");
                        }
                        break;
                    case 1:
                        set("移動先の座標に駒台は指定できません もう一度移動前座標入力からやり直してください");
                        break;
                }
            }
        }
    }

}
