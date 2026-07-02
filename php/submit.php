<?php
// Import PHPMailer classes into the global namespace
use PHPMailer\PHPMailer\PHPMailer;
use PHPMailer\PHPMailer\SMTP;
use PHPMailer\PHPMailer\Exception;

// Load Composer's autoloader
require '../vendor/autoload.php';

// ==========================================
// CONFIGURATION (UPDATE THESE VALUES)
// ==========================================
$gmail_username = 'muba4shir@gmail.com'; // e.g. woodberrydesigns@gmail.com
$gmail_app_password = 'vthsvermucinmwqx';        // 16-character App Password from Google
$receive_email = 'info@woodberrydesigns.com';     // Where you want to receive the inquiries
// ==========================================

$mail = new PHPMailer(true);

try {
    // Assigning data from $_POST array to variables
    $name = isset($_POST['name']) ? $_POST['name'] : 'No Name';
    $from = isset($_POST['email']) ? $_POST['email'] : 'No Email';
    $phone = isset($_POST['phone']) ? $_POST['phone'] : 'No Phone';
    $message = isset($_POST['message']) ? $_POST['message'] : 'No Message';

    // Server settings
    // $mail->SMTPDebug = SMTP::DEBUG_SERVER;      // Enable verbose debug output (uncomment for troubleshooting)
    $mail->isSMTP();                               // Send using SMTP
    $mail->Host       = 'smtp.gmail.com';          // Set the SMTP server to send through
    $mail->SMTPAuth   = true;                      // Enable SMTP authentication
    $mail->Username   = $gmail_username;           // SMTP username
    $mail->Password   = $gmail_app_password;       // SMTP password
    $mail->SMTPSecure = PHPMailer::ENCRYPTION_STARTTLS; // Enable TLS encryption
    $mail->Port       = 587;                       // TCP port to connect to

    // Recipients
    // The "From" address must be your Gmail address when using Gmail SMTP to avoid being marked as spam
    $mail->setFrom($gmail_username, 'Woodberry Website Form');
    // We add the submitter's email as the Reply-To so you can hit "Reply" in your email client
    $mail->addReplyTo($from, $name);
    // Where the email will be sent
    $mail->addAddress($receive_email);

    // Content
    $mail->isHTML(false);                          // Set email format to plain text
    $mail->Subject = 'Contact Inquiry: ' . $name;
    
    $body_message = "Name: " . $name . "\r\n";
    $body_message .= "Email: " . $from . "\r\n";
    $body_message .= "Phone: " . $phone . "\r\n";
    $body_message .= "Message:\r\n" . $message . "\r\n";

    $mail->Body = $body_message;

    // Send the email
    $mail->send();
    ?>
    <script language="javascript" type="text/javascript">
        window.alert("Sent Successfuly.");
    </script>
    <?php
} catch (Exception $e) {
    ?>
    <script language="javascript" type="text/javascript">
        window.alert("Error! Please Try Again Later. Mailer Error: <?php echo addslashes($mail->ErrorInfo); ?>");
    </script>
    <?php
}
