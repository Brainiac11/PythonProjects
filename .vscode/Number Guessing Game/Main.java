import java.awt.*;
import java.awt.event.*;
import javax.swing.*;

public class BouncingBall extends JPanel {
  // define ball properties
  private int x = 200;
  private int y = 200;
  private int radius = 20;
  private int dx = 2;
  private int dy = 2;

  // define animation properties
  private int width = 400;
  private int height = 400;
  private int delay = 10;

  // define the paint method to draw each frame of the animation
  public void paint(Graphics g) {
    // draw the ball at its current position
    g.fillOval(x - radius, y - radius, radius * 2, radius * 2);

    // update the ball's position by adding the velocity
    x += dx;
    y += dy;

    // check if the ball has reached the edge of the window
    // and reverse the corresponding velocity if necessary
    if (x - radius < 0 || x + radius > width) {
      dx = -dx;
    }
    if (y - radius < 0 || y + radius > height) {
      dy = -dy;
    }
  }

  public static void main(String[] args) {
    // create a new JFrame to display the animation
    JFrame window = new JFrame("Bouncing Ball");
    window.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    window.setVisible(true);
  }
}