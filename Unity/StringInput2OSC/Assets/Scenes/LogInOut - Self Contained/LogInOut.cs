using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using TMPro;
public class LogInOut : MonoBehaviour
{
    [SerializeField] private float loginTimeSec = 1f;
    [SerializeField] private float logoutTimeSec = 1f;
    [SerializeField] private TextMeshProUGUI displayText;
    
    [SerializeField] private const float timeoutSeconds = 5;
    private Coroutine loginCoroutine;
    private Coroutine logoutCoroutine;
    private float loginProgress = 0f;
    private float logoutProgress = 0f;    
    private string currentText;
    private string loginText = "Press '1' to Login";

    private string instructions =
        "Use Trackpad to Move, Tap to Jump.\n Type a question to your AI friend and press 'Enter' to send message.";
    private float timeElapsed;
    private bool loggedIn = false;

    void Start()
    {
        currentText = loginText;
    }
    void Update()
    {

        userLogInOut();
        
        if (loggedIn)
        {
            timeElapsed += Time.deltaTime;
            AutoLogout();
        }
    }
    void userLogInOut()
    {
        if (Input.GetKeyDown(KeyCode.Alpha1) && !loggedIn)
        {
            loggedIn = true;
            loginCoroutine = StartCoroutine(Login());

        }
        if (Input.GetKeyDown(KeyCode.Alpha2) && loggedIn)
        {
            loggedIn = false;
            logoutCoroutine = StartCoroutine(Logout());
        }
    }

    IEnumerator Login()
    {
        Debug.Log("Logging In");
        
        //CALL CHAT HISTORY TO START SAVING CHAT (NEEDED?)
        
        while (loginProgress < loginTimeSec)
        {
            loginProgress += Time.deltaTime;
            yield return null;
        }
        currentText = instructions;
        timeElapsed = 0f; //reset timeout counter
        loginProgress = 0f;
        displayText.text = currentText;
        Debug.Log("Logged In");
    }
    IEnumerator Logout()
    {
        Debug.Log("Logging Off");
        
        //CALL CHAT HISTORY TO WRITE BUFFER TO .TXT THEN CLEAR
        
        timeElapsed = 0f;
        while (logoutProgress < logoutTimeSec)
        {
            logoutProgress += Time.deltaTime;
            yield return null;
        }
        currentText = loginText;
        logoutProgress = 0f;
        Debug.Log("Logged Out");
        displayText.text = currentText;
    }
    void AutoLogout()
    {
        if(timeElapsed > timeoutSeconds)
        {
            StartCoroutine(Logout());
        }
    }
}
