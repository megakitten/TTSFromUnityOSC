using UnityEngine;
using TMPro;

public class AutoSelect : MonoBehaviour
{
    [SerializeField] private TMP_InputField InputField;
        
    // Start is called before the first frame update
    void Start()
    {
        InputField.Select();
    }

}
