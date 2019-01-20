//
//  SettingsViewController.swift
//  Fruit Detection
//
//  Created by Dhaval Gogri on 11/21/18.
//  Copyright © 2018 Dhaval Gogri. All rights reserved.
//

import UIKit

class SettingsViewController: UIViewController, UITextFieldDelegate {

    @IBOutlet weak var textViewDSID: UITextField!
    @IBOutlet weak var textViewIPAddress: UITextField!
    
    @IBOutlet weak var buttonSave: UIButton!
    
    let defaults = UserDefaults.standard
    
    override func viewDidLoad() {
        super.viewDidLoad()
        self.textViewDSID.delegate = self
        self.textViewIPAddress.delegate = self
        
        if(defaults.integer(forKey: "DSID") == 0){
            self.textViewDSID.text = "1"
        }
        else{
            self.textViewDSID.text = String(defaults.integer(forKey: "DSID"))
        }
        
        
        if(defaults.string(forKey: "IP_ADDRESS") == ""){
            self.textViewIPAddress.text = "http://10.8.105.18:8000"
        }
        else{
            self.textViewIPAddress.text = defaults.string(forKey: "IP_ADDRESS")
        }
        
        self.saveInformation(buttonSave)
        
    }
    

    /*
    // MARK: - Navigation

    // In a storyboard-based application, you will often want to do a little preparation before navigation
    override func prepare(for segue: UIStoryboardSegue, sender: Any?) {
        // Get the new view controller using segue.destination.
        // Pass the selected object to the new view controller.
    }
    */
    @IBAction func saveInformation(_ sender: Any) {
        if(self.textViewDSID.text=="" || self.textViewIPAddress.text!==""){
            showAlertBox("Information Missing. Please Enter information in all the text boxes")
            return
        }
            
        self.defaults.set(Int(self.textViewDSID.text!), forKey: "DSID")
        self.defaults.set(self.textViewIPAddress.text, forKey: "IP_ADDRESS")
        self.showAlertBox("Information Saved")
        
    }
    
    func textFieldShouldReturn(_ textField: UITextField) -> Bool {
        textField.resignFirstResponder()
        return true
    }
    
    func showAlertBox(_ message: String?) {
        let alert = UIAlertController(title: "ALERT", message: message, preferredStyle: .alert)
        
        // Only when the user presses the 'GOT IT!' button, the game scene is created
        let okButton = UIAlertAction(title: "GOT IT!", style: .default, handler: { action in
            
            alert.dismiss(animated: true)
            
        })
        
        alert.addAction(okButton)
        present(alert, animated: true)
    }
    
}
