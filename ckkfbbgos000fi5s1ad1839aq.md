## How to Install Java & Set Environment Variables

<p>In this course, we will study the <a href="https://usemynotes.com/how-to-install-java/">How to Install Java</a> and how to Set Environment Variables in java and Installation of Java in Windows Operating System</p>
<h2>How to install Java?</h2>
<p>Java is supported in many platforms like Windows, Linux, Solaris, etc. All these platforms have their own installation methods. We will not be covering installation procedures for all the platforms that support Java but only Windows operating system for the moment.</p>
<h2>Installation of Java in Windows Operating System</h2>
<p>Whether you are using a 32-bit operating system or a 64-bit operating system. Both of them have a similar installation procedure.</p>
<h3>Step 0: Check if you already have Java installed on your computer.</h3>
<p>Most of today’s desktop applications require Java to work. They require Java to be installed on the host system to properly get executed. So if you have one of those applications in your computer then you probably might have Java already installed on your computer.</p>
<p>To confirm whether you have Java installed on your computer or not, follow these steps -</p>
<ol>
<li>Hold the <strong>Windows key</strong> and press <strong>R</strong> on your keyboard. This will open up the Run dialog box.</li>
<li>Now enter <strong>cmd</strong> in that dialog box and click <strong>OK</strong>. This is open to the Command Prompt window.</li>
<li>In the <strong>Command Prompt</strong>, type <strong>java -version</strong> and press <strong>Enter</strong> on your keyboard.</li>
<li>If you see this type of output below with java version, then congratulations you have Java installed on your computer and no need to continue to further steps.</li>
<li>If you don’t see an output similar to the above image, then follow the next step.</li>
</ol>
<h3>Step 1: Know whether you have a 32-bit or 64-bit operating system.</h3>
<p>Knowing your operating system type is important for installing Java. It comes for both 32-bit and 64-bit operating systems. If you know the type of operating system you have to install Java then you can move to the next step. If you don’t know your system type or having trouble finding it out then follow these simple steps:</p>
<ol>
<li>Open <strong>File Explore</strong>r that comes with your Windows operating system.</li>
<li>On the left side panel, Right-click on <strong>This PC</strong> to open the context menu and then click on <strong>Properties</strong>.</li>
<li>This will open up the <strong>System Properties</strong> of your computer. Now, under the <strong>System</strong>section, check out the <strong>System type</strong> of your computer.</li>
</ol>
<h3>Step 2: Download Java Development Kit (JDK)</h3>
<ul>
<li>Head to the official Java download website to browse through the JDK packages. Link: (<a href="https://www.oracle.com/java/technologies/javase/javase-jdk8-downloads.html"real="nofollow">https://www.oracle.com/java/technologies/javase/javase-jdk8-downloads.html)</li>
<li>Scroll down the page in the link given above and click on the appropriate link based on the operating system you wish to install.</li>
<li>A pop window may appear to accept the license agreement. If you wish to read it then you can or just select the checkbox accepting the license agreement and click the Download button. </li>
<li>You will then be redirected to a login page where you will have to sign in to start the download.</li>
<ol>
  <li>Don’t have an Oracle Account? Follow this link to create one. Link: (https://profile.oracle.com/myprofile/account/create-account.jspx)</li>
  <li>Already have an Oracle Account? Then fill out the username and password and sign in to start the download.</li>
</ol>
<li>Once downloaded, open the installer package and follow the installation wizard. During installation, you may change the installation path if needed. But the default settings during installation is recommended.</li>
</ul>
<p>After the completion of the installation, just repeat<strong> Step 0</strong> to check whether the installation is successful.</p>
<h2>Setting up Environment Variable</h2>
<p>Environment variables are set to enable the system to access externally installed applications or executables. These variables are in the form of a Key-Value pair. They are generally used by the system and other applications to access an external application or program that does a specific task.</p>
<p>We will set environment variables to make sure our system has access to Java. Also, it will enable us to use Java executables globally in a system</p>
<h2>How to set environment variables for Java in Windows 10?</h2>
<ol>
<li>Locate the Java installation on your PC. If you have installed Java using default options, then it can be located in one of the following locations:</li>
 <table class="table table-bordered table-striped">
  <thead>
    <tr>
      <td>C:/Program Files/Java/jdk-&lt;version> /bin&nbsp;&nbsp;&nbsp;&nbsp; - For 64-bit OS<br>
C:/Program Files (x86)/Java/jdk-&lt;version>/bin&nbsp;&nbsp;&nbsp;&nbsp;- For 32-bit OS</td>
    </tr>
  </thead>
</table>
<p>Copy the location of the bin folder of the Java installation which contains java and javac.</p>
<li>Open <strong>File Explorer</strong> that comes with your Windows operating system.</li>
<li>On the left side panel, Right-click on <strong>This PC</strong> to open the context menu and then click on <strong>Properties</strong>.</li>
<li>This will open up the <strong>System Properties</strong> of your computer. On the left panel, click on <strong>Advanced system settings</strong>.</li>
<li>Under the <strong>Advanced tab</strong>, click on <strong>Environment Variables</strong>.</li>
<li>Under the <strong>System Variables</strong> section, locate the <strong>Path</strong> variable and double-click on it. (If there is no <strong>Path</strong> variable then create a new one)</li>
<li>Click on <strong>New</strong> and paste the location of the <strong>bin</strong> folder of the Java installation from step 1 and click on <strong>OK</strong>.</li>
<li>You have successfully set the Java environment variable. Now you may close all the other dialog boxes that were opened since step 1.</li>
</ol>