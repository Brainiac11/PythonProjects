package PlatformerGame;
import java.awt.event.ActionListener;
import java.awt.event.ActionEvent;
import java.util.Timer;

public class GamePanel extends javax.swing.JPanel implements ActionListener {
    Player player;
    Timer gameTimer;

    public GamePanel() {
        gameTimer = new Timer();
        gameTimer.schedule(new TimerTask());
    }
    public void actionPerformed(ActionEvent ae){
    }
}

