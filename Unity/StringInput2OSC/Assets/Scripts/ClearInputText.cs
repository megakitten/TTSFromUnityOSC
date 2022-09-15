using TMPro;
using UnityEngine;
using OscCore;
public class ClearInputText : MonoBehaviour
{
    [SerializeField] private TMP_InputField inputField;
    private OscClient client = new OscClient("127.0.0.1", 8001);

    void Start()
    {
        //InputField.text = "[ User Input ]";
        inputField.Select();
    }

    // Update is called once per frame
    void Update()
    {
        if(Input.GetKeyDown(KeyCode.Return))
        {
            // TO DO: Send text through OSC 
            // TO DO: Add GPT support
            client.Send("/user_input", inputField.text);
            inputField.text = "";
            inputField.Select();
        }
    }
}

