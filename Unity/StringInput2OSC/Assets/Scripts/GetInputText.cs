using TMPro;
using UnityEngine;

public class GetInputText : MonoBehaviour
{
    [SerializeField] private TMP_InputField inputField;
        
    // Start is called before the first frame update
    void Start()
    {
        //inputField.text = "[ User Input ]";
        inputField.Select();

    }

    // Update is called once per frame
    void Update()
    {
        if(Input.GetKeyDown(KeyCode.Return))
        {
            // TO DO: Send text through OSC 
            // TO DO: Add GPT support
            inputField.text = "";
        }
    }
}
