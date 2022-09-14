
using TMPro;
using UnityEngine;

public class GetInputText : MonoBehaviour
{
    [SerializeField] private TMP_InputField InputField;
        
    // Start is called before the first frame update
    void Start()
    {
        InputField.text = "Hey Bitch! What's on your mind?";
    }

    // Update is called once per frame
    void Update()
    {
        if(Input.GetKeyDown(KeyCode.Return))
        {
            // TO DO: Send text through OSC 
            // TO DO: Add GPT support
            InputField.text = "";
        }
    }
}
