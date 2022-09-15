using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using TMPro;

public class SetText : MonoBehaviour
{
    [SerializeField] private TMP_InputField inputField;

    [SerializeField] private string prompt;
    
    // Start is called before the first frame update
    void Start()
    {
        inputField.text = prompt;
    }
}
